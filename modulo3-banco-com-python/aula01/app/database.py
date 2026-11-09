<<<<<<< HEAD
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão SQLite -- aponta para o arquivo .db
# O './' significa a pasta raiz do projeto
DB_URL = 'sqlite:///./funcionarios.db'

# Engine: a conexão com o banco
engine = create_engine(
    DB_URL,
    echo=True,              # imprime o SQL no terminal
    connect_args={'check_same_thread': False},  # necessário para SQLite
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão SQlite - aponta para o arquivo .db
# 0 './' significa a pasra raiz do projeto
DB_URL = 'sqlite:///./funcionarios.db'

#Engine: é a conexão com o banco
engine = create_engine(
    DB_URL,
    echo=True,       # imprime o SQL no terminal
    connect_args={'check_same_thread': False}, # Necessário para SQlite
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
)

# SessionLocal: fábrica de sessões
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base: classe pai de todos os modelos ORM
class Base(DeclarativeBase):
<<<<<<< HEAD
    pass
=======
    pass
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
