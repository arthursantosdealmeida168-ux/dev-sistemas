from app.database import SessionLocal
from app.models import Curso, Aluno

def popular_banco():
    db = SessionLocal()
    try:
        if db.query(Curso).count() > 0:
            print('Banco já populado. Pulando...')
            return
        db.add_all([
            Curso(nome='Desenvolvimento de Sistemas', duracao=1200),
            Curso(nome='Desenvolvimento Web', duracao=1000),
            Curso(nome='Banco de Dados', duracao=800),
        ])
        db.add_all([
            Aluno(nome='Lucas Mendes', email='lucas@senai.com', matricula='2025001'),
            Aluno(nome='Ana Silva', email='ana@senai.com', matricula='2025002'),
            Aluno(nome='Carlos Souza', email='carlos@senai.com', matricula='2025003'),
            Aluno(nome='Mariana Santos', email='mariana@senai.com', matricula='2025004'),
        ])
        db.commit()
        print('Banco populado com sucesso!')
    except Exception as e:
        db.rollback()
        print(f'Erro: {e}')
    finally:
        db.close()

if __name__ == '__main__':
    popular_banco()