from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

<<<<<<< HEAD
# URL do banco SQLite - Cria o arquivo estoque.db na raiz do projeto
=======
# URL do banco SQLite - Criar o arquivo estoque.db na raiz do projeto
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
DATABASE_URL = "sqlite:///./estoque.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass