from app.database import engine, SessionLocal
from app import models
from app.models import Genero, Autor, Livro

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

genero_ficcao = Genero(nome="Ficção Científica")
genero_romance = Genero(nome="Romance")
genero_terror = Genero(nome="Terror")

db.add(genero_ficcao)
db.add(genero_romance)
db.add(genero_terror)
db.commit()
db.refresh(genero_ficcao)
db.refresh(genero_romance)
db.refresh(genero_terror)

autor_machado = Autor(nome="Machado de Assis", nacionalidade="Brasileira")
autor_rowling = Autor(nome="J.K. Rowling",nacionalidade="Britânica")
autor_king = Autor(nome="Stephen King", nacionalidade="norte-americano")

db.add(autor_machado)
db.add(autor_rowling)
db.add(autor_king)
db.commit()
db.refresh(autor_machado)
db.refresh(autor_rowling)
db.refresh(autor_king)

livros = [
    Livro(titulo="Dom Casmurro", ano_publicacao=1899, disponivel=True, genero_id=genero_romance.id, autor_id=autor_machado.id),

    Livro(titulo="Harry Potter", ano_publicacao=1997, disponivel=True, genero_id=genero_ficcao.id, autor_id=autor_rowling.id),

    Livro(titulo="It: A coisa", ano_publicacao=1986, disponivel=True, genero_id=genero_terror.id, autor_id=autor_king.id),

    Livro(titulo="Carrie, a Estranha", ano_publicacao=1974, disponivel=True, genero_id=genero_terror.id, autor_id=autor_king.id),

    Livro(titulo="Quincas Borba", ano_publicacao=1891, disponivel=True, genero_id=genero_romance.id, autor_id=autor_machado.id),
]
for p in livros:
    db.add(p)
db.commit()
print(f' {len(livros)} livros inseridos')
db.close()