# Definir modelo de tabelas
from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

class Categoria(Base):
<<<<<<< HEAD
    __tablename__ = "categorias"
=======
    __tablename__= "categorias"
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)

class Fornecedor(Base):
<<<<<<< HEAD
    __tablename__ = "fornecedores"
=======
    __tablename__= "fornecedores"
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False)
    contato = Column(String(80), nullable=False)

class Produto(Base):
<<<<<<< HEAD
    __tablename__ = "produtos"
=======
    __tablename__= "produtos"
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
<<<<<<< HEAD
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    
=======
    fornecedor_id = Column( Integer, ForeignKey("fornecedores.id"))  
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
