from app.database import engine, Base, SessionLocal
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Jorge simas', 'jorge@gmail.com', '(66) 99085-8321', 3300.0)
    print(f'Criado: {novo}')
finally:
    db.close()