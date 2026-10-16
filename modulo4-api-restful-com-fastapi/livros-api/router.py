from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Livro
from schemas import LivroCreate, LivroPatch, LivroResponse

router = APIRouter(prefix='/livros', tags=['Livros'])

@router.get('/', response_model=List[LivroResponse])
def listar_livros(skip: int=3, limit: int=10, db: Session = Depends(get_db)):
    return db.query(Livro).offset(skip).limit(limit).all()

@router.get('/{livro_id}', response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail=F'Livro {livro_id} não encontrado')
    return livro


@router.post('/', response_model=LivroResponse, status_code=201)
def criar_livro(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(
      titulo = dados.titulo,
      autor = dados.autor,
      ano_publicacao = dados.ano_publicacao,
      disponivel = dados.disponivel,
    )
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro

@router.patch('/{livro_id}', response_model=LivroResponse)
def atualizar_livro(livro_id: int, dados: LivroPatch, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail='Não Encontrado')
    if dados.titulo is not None: livro.titulo = dados.titulo
    if dados.autor is not None: livro.autor = dados.autor
    if dados.ano_publicacao is not None: livro.ano_publicacao = dados.ano_publicacao
    if dados.disponivel is not None: livro.disponivel = dados.disponivel
    db.commit()
    db.refresh(livro)
    return livro

@router.delete('/{livro_id}')
def remover_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail='Não Encontrado')
    livro.ativo = False
    db.commit()
    return {'mesangem': F'Livro_id removido com sucesso!'}