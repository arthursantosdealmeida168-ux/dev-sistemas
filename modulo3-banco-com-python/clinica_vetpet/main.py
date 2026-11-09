<<<<<<< HEAD
from app.database import engine, SessionLocal, Base
from app import models
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento

# Cria todas as tabelas (na ordem correta — SQLAlchemy resolve as FKs)
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    try:
        # Tutores
        t1 = inserir_tutor(db, "Max Muller", "(61) 98888-1111", "max@email.com")
        t2 = inserir_tutor(db, "Alanna", "(61) 97777-2222", "alanna@email.com")
        t3 = inserir_tutor(db, "Sandra", "(61) 96666-3333", "sandra@email.com")

        print(f"Tutores cadastrados: {t1.nome_completo}, {t2.nome_completo}, {t3.nome_completo}")

        # Animais
        a1 = inserir_animal(db, "Ted", "Cachorro", "Labrador", 32.5, t1.id)
        a2 = inserir_animal(db, "Tom", "Gato", "Persa", 4.2, t2.id)
        a3 = inserir_animal(db, "Bolinha","Cachorro", "SRD", 8.0, t1.id)
        a4 = inserir_animal(db, "Nina", "Gato", "Siamês", 3.8, t3.id)
        a5 = inserir_animal(db, "Freddie", "Cachorro", "Golden", 28.0, t2.id)

        print(f"Animais cadastrados: {a1.nome_animal}, {a2.nome_animal}, {a3.nome_animal}, "
              f"{a4.nome_animal}, {a5.nome_animal}")

        # Atendimentos
        at1 = inserir_atendimento(db, "01/10/2025", "Consulta de rotina", 150.00, a1.id)
        at2 = inserir_atendimento(db, "02/10/2025", "Vacina antirrábica", 80.00, a2.id)
        at3 = inserir_atendimento(db, "03/10/2025", "Banho e tosa", 60.00, a3.id)
        at4 = inserir_atendimento(db, "04/10/2025", "Exame de sangue", 120.00, a4.id)
        at5 = inserir_atendimento(db, "05/10/2025", "Castração", 350.00, a5.id)
        at6 = inserir_atendimento(db, "06/10/2025", "Retorno pós-cirúrgico", 80.00, a5.id)
        at7 = inserir_atendimento(db, "07/10/2025", "Consulta — problema de pele", 150.00, a1.id)

        print(f"Atendimentos registrados: {at1.id}, {at2.id}, {at3.id}, "
              f"{at4.id}, {at5.id}, {at6.id}, {at7.id}")

        print("\nBanco populado com sucesso! Arquivo: clinica_vetpet.db")

    finally:
        db.close()


if __name__ == "__main__":
    main()
=======
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
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
