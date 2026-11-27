from fastapi import FastAPI
from database import engine, Base
import models
from routers import plataformas, jogos, avaliacoes
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Loja de games API",
    description="Gerenciador de catálago de jogos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)

@app.get("/")
def raiz():
    return {"mensagem": "Loja de games API funcionado!"}
