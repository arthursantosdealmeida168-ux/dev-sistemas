from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Jogo
from tags import tags_metadata

router = APIRouter(prefix="/jogos", tags=["Jogos"])

class JogoCreate(BaseModel):
    titulo: str
    genero: str
    preco: float
    plataforma_id: int

def get_or_404(jogo_id: int, db: Session) -> Jogo:
    jogo = db.query(jogo).filter(jogo.id == jogo_id).first()
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return jogo

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Jogo).all()

@router.get("/{jogo_id}")
def buscar(jogo_id: int, db: Session = Depends(get_db)):
    return get_or_404(jogo_id, db)

@router.put("/{jogo_id}")
def atualizar(jogo_id: int, dados: Jogo, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)

    jogo.titulo = dados.titulo
    jogo.genero = dados.genero
    jogo.preco = dados.preco
    db.commit()
    db.refresh(jogo)
    return jogo

@router.delete("/{jogo_id}")
def deletar(jogo_id: int, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)

    db.delete(jogo)
    db.commit()
    return{"mensagem": "Jogo não encontrado"}

@router.get("/{jogo_id}/avaliacoes")
def listar(jogo_id: int, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)
    return jogo.avaliacoes