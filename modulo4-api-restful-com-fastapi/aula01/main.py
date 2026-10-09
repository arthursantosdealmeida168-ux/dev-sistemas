from fastapi import FastAPI
from database import engine, Base
from router import router as produto_router

# Criar as tabelas no banco ao inicial a API
# Se o  banco.db não existir, cria o arquivo e as tabelas
# Se o já existir, não faz nada - não apaga os dados
Base.medatada.create_all(bin=engine)

app = FastAPI(
    title="API de Produtos - SENAI",
    description="CRUD com FastApi + SQLALchemy + SQLite",
    version="2.0.0"
)

# Registra o router com prefixo/produtos
app.include_router(produto_router)

@app.get('/')
def raiz():
    return {"status": "online", "docs":"/docs", "versao":"2.0.0"}