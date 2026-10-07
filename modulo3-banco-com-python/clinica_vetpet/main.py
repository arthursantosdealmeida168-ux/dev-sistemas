from app.database import engine, SessionLocal
from app import models
from app.models import Tutor, Animal, Atendimento

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:

    tutor1 = Tutor(
        nome_completo="Rafael de Sousa",
        telefone="(11) 99135-3352",
        email="rafael.email@br"
    )
    tutor2 = Tutor(
        nome_completo="Yasmin santos",
        telefone="(55) 99254-7568",
        email="yasmin.email@br"
    )

    db.add_all([tutor1, tutor2])
    db.commit()

    db.refresh(tutor1)
    db.refresh(tutor2)

    print(f"Tutor inserido: {tutor1.nome_completo} (id={tutor1.id})")
    print(f"Tutor inserido: {tutor2.nome_completo} (id={tutor2.id})")

    animal1 = Animal(
        nome_animal="Bibo",
        especie="cão",
        tutor_id=tutor1.id
    )
    animal2 = Animal(
        nome_animal="Kitty",
        especie="gato",
        tutor_id=tutor1.id
    )
    animal3 = Animal(
        nome_animal="Pedro",
        especie="coelho",
        tutor_id=tutor2.id
    )

    db.add_all([animal1, animal2, animal3])
    db.commit()

    db.refresh(animal1)
    db.refresh(animal2)
    db.refresh(animal3)

    print(f"Animal inserido: {animal1.nome_animal} - {animal1.especie} (id={animal1.id})")
    print(f"Animal inserido: {animal2.nome_animal} - {animal2.especie} (id={animal2.id})")
    print(f"Animal inserido: {animal3.nome_animal} - {animal3.especie} (id={animal3.id})")

    atendimento1 = Atendimento(
        motivo="Vacina anual V8",
        valor_cons=150.00,
        data_atend="07/10/2026",
        animal_id=animal1.id
    )
    atendimento2 = Atendimento(
        motivo="Consulta de rotina e check-up",
        valor_cons=120.00,
        data_atend="07/10/2026",
        animal_id=animal2.id
    )
    atendimento3 = Atendimento(
        motivo="Corte de dentes e unhas",
        valor_cons=90.00,
        data_atend="07/10/2026",
        animal_id=animal3.id
    )

    db.add_all([atendimento1, atendimento2, atendimento3])
    db.commit()

    print(f"Atendimento: {atendimento1.motivo} | R$ {atendimento1.valor_cons:.2f}")
    print(f"Atendimento: {atendimento2.motivo} | R$ {atendimento2.valor_cons:.2f}")
    print(f"Atendimento: {atendimento3.motivo} | R$ {atendimento3.valor_cons:.2f}")

finally:
    db.close()