from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
<<<<<<< HEAD
DB_URL = 'sqlite:///./escola.db'
engine = create_engine(DB_URL, echo=True, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
class Base(DeclarativeBase):
    pass

=======
DB_URL = 'sqlite:///./escola.db' 
engine = create_engine(DB_URL, echo=True, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
