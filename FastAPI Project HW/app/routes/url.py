"""
Эндпоинты авторизации пользователя, сокращения URL, статистики, генерации QR
"""
import os
from fastapi import Request, HTTPException, APIRouter, Depends
from fastapi.responses import RedirectResponse, FileResponse
import qrcode
from app.db.session import get_session
from app.models.models import URL
from app.schemas.schemas import URLRequest
from app.core.security import get_current_user

router = APIRouter()

@router.post("/short_link")
def short_link(data: URLRequest, request: Request, user = Depends(get_current_user), session=Depends(get_session)):
    """
    URL и QR-код
    
    Аргументы:
        data: оригинальная ссылка
        user: пользователь

    """
    url = URL(original_url=data.user_url, owner=user.username)
    session.add(url)
    session.commit()
    session.refresh(url)
    
    short_url = f"{request.base_url}{url.id}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data.user_url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    os.makedirs("qrcodes", exist_ok=True)
    
    qr_path = f"qrcodes/{url.id}.png"
    qr_image.save(qr_path)
    
    url.qr_code_path = qr_path
    session.add(url)
    session.commit()
    
    return {
        "short_url": short_url,
        "qr_code_path": f"/qr/{url.id}"
    }

@router.get("/{short_id}")
def redirect(short_id: str, session=Depends(get_session)):
    """Счетчик кликов"""
    url = session.get(URL, short_id)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    url.clicks += 1
    session.add(url)
    session.commit()
    return RedirectResponse(url=url.original_url)

@router.get("/stats/{short_id}")
def stats(short_id: str, session=Depends(get_session)):
    """Статистика кликов"""
    url = session.get(URL, short_id)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"clicks": url.clicks}

@router.get("/qr/{short_id}")
def get_qr_code(short_id: str, session=Depends(get_session)):
    """Изображение QR-кода"""
    url = session.get(URL, short_id)
    if not url or not url.qr_code_path:
        raise HTTPException(status_code=404, detail="QR code not found")
    if not os.path.exists(url.qr_code_path):
        raise HTTPException(status_code=404, detail="QR code file not found")
    return FileResponse(url.qr_code_path)