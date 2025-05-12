"""
Сокращение URL
SQLModel модели для URL and Users
"""
from typing import Optional
import uuid
from sqlmodel import SQLModel, Field


class URL(SQLModel, table=True):
    """Сокращение URL"""
    id: str = Field(default_factory=lambda: uuid.uuid4().hex[:6], primary_key=True)
    original_url: str
    clicks: int = 0
    owner: str
    qr_code_path: Optional[str] = None


class User(SQLModel, table=True):
    """User аутентификация и авторизация"""
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str