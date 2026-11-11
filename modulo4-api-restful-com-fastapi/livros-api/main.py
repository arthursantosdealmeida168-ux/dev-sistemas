from fastapi import FastAPI
from database import engine, Base
from router import router as livro_router
from tags import tags_metadata

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de livros - SENAI",
    description="CRUD com FastApi + SQLALchemy + SQLite",
    version="2.0.0"
)

# Configuração do FastApi - agora com metadados do Swagger
app = FastAPI(
    title='API de livros - SENAI',
    description="""
## API de gerenciamento de tarefas
Rotas de criação, edição e exclusão exigem autenticação JWT
""",
    version='1.1.0',
    openapi_tags=tags_metadata,)


app.include_router(livro_router)

@app.get('/')
def raiz():
    return {"status": "online", "docs":"/docs", "versao":"2.0.0"}