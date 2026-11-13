from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from pydantic import BaseModel, Field
from models import Avaliacoe
from tags import tags_metadata

router = APIRouter(prefix="/avaliacoes", tags=["Avaliacoes"])

class AvaliacoeCreate(BaseModel):
    nota: int = Field(..., ge=1, le=5) #entre 1 e 5
    comentario: str
    jogo_id: int

def get_or_404(avaliacoe_id: int, db: Session) -> Avaliacoe:
    avaliacoe = db.query(avaliacoe).filter(avaliacoe.id == avaliacoe_id).first()
    if not avaliacoe:
        raise HTTPException(status_code=404, detail="Avaliaçõe foi deletada")
    return avaliacoe

@router.post("/", status_code=201, summary="O jogo foi avaliado",
             responses={409: {"description": "Avaliaçõe de jogo foi criada"}})
def criar(dados: AvaliacoeCreate, db: Session = Depends(get_db)):
    existe = db.query(Avaliacoe).filter(Avaliacoe.nota == dados.nota).first()
    if existe:
        raise HTTPException(status_code=409, detail="Avaliaçõe de jogo foi criada")
    nova = Avaliacoe(nota=dados.nota)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.delete("/{avaliacoe_id}")
def deletar(avaliacoe_id: int, db: Session = Depends(get_db)):
    avaliacoe = get_or_404(avaliacoe_id, db)

    db.delete(avaliacoe)
    db.commit()
    return{"mensagem": "Avaliaçõe foi deletada"}