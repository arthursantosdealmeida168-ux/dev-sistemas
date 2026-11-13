from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Plataforma
from tags import tags_metadata

router = APIRouter(prefix="/plataformas", tags=["Plataformas"])

class PlataformaCreate(BaseModel):
    id: str
    nome: str

def get_or_404(plataforma_id: int, db: Session) -> Plataforma:
    plataforma = db.query(plataforma).filter(plataforma.id == plataforma_id).first()
    if not plataforma:
        raise HTTPException(status_code=404, detail="Plataforma não encontrada")
    return plataforma    

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Plataforma).all()

@router.post("/", status_code=201, summary="Cadastrar plataforma",
             responses={409: {"description": "Plataforma já cadastrada"}})
def criar(dados: PlataformaCreate, db: Session = Depends(get_db)):
    existe = db.query(Plataforma).filter(Plataforma.nome == dados.nome).first()
    if existe:
        raise HTTPException(status_code=409, detail="Plataforma já cadastrada")
    nova = Plataforma(nome=dados.nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova