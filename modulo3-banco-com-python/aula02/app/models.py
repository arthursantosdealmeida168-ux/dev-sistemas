from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Departamento(Base):
<<<<<<< HEAD
    __tablename__ = 'departamentos' # nome da tabela no banco
=======
    __tablename__= 'departamentos' # nome da tabela no banco
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sigla = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Departamento id={self.id} nome={self.nome}>'

class Cargo(Base):
    __tablename__ = 'cargos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    nivel = Column(String(20), nullable=False)
    salario_min = Column(Float, nullable=False)
    salario_max = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Cargo {self.titulo} {self.nivel}>'
<<<<<<< HEAD
=======

>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
    nome = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20), nullable=True)
    salario = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)
    
    def __repr__(self):
        return f'<Funcionario id={self.id} nome={self.nome}>'
=======
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    salario = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Funcionario {self.nome}>'
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
