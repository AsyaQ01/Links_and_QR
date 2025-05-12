from sqlmodel import create_engine, SQLModel


engine = create_engine("sqlite:///./urls.db")
SQLModel.metadata.create_all(engine)

def init_db():
    """Иницилизация БД"""
    SQLModel.metadata.create_all(engine)