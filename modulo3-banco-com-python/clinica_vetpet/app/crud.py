from sqlalchemy.orm import Session
from app.models import Tutor, Animal, Atendimento

def criar_tutor(db: Session, nome: str, telefone: str, email:str):
    tut = Tutor(nome=nome, telefone=telefone, email=email)
    db.add(tut)
    db.commit()
    db.refresh(tut)
    return tut

def criar_animal(db: Session, nome: str, especie: str, raca:str, peso_kg: int, tutor_id: int):
    ani = Animal(nome=nome, especie=especie, raca=raca, peso_kg=peso_kg, tutor_id=tutor_id)
    db.add(ani)
    db.commit()
    db.refresh(ani)
    return ani

def criar_atendimento(db: Session, nome: str, data_atend: int, motivo: str, valor_cons: float, animal_id: int):
    ate = Atendimento(nome=nome, data_atend=data_atend, motivo=motivo, valor_cons=valor_cons, animal_id=animal_id)
    db.add(ate)
    db.commit()
    db.refresh(ate)
    return ate