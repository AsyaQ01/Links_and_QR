from pydantic import BaseModel, validator


class URLRequest(BaseModel):
    """Оригинальная ссылка"""
    user_url: str


class Token(BaseModel):
    """
    access_token: JWT токен для авторизации
    token_type: токен типа "bearer

    """

    access_token: str
    token_type: str