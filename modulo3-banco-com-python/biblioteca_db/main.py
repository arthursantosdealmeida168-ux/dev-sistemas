from app.database import engine, SessionLocal
from app import models
from app.models import Genero, Autor, Livro

models.Base.metadata.create_all(bind=engine)
<<<<<<< HEAD
print("Tabelas criadas")

db = SessionLocal()

g1 = Genero(nome="Ficção Científica")
g2 = Genero(nome="Romance")
g3 = Genero(nome="Terror")
db.add(g1); db.add(g2); db.add(g3)
db.commit()
db.refresh(g1); db.refresh(g2); db.refresh(g3)

a1 = Autor(nome="Isaac Asimov", nacionalidade="Americano")
a2 = Autor(nome="Machado de Assis", nacionalidade="Brasileiro")
a3 = Autor(nome="Stephen King", nacionalidade="Americano")
db.add(a1); db.add(a2); db.add(a3)
db.commit()
db.refresh(a1); db.refresh(a2); db.refresh(a3)

livros = [
    Livro(titulo="Fundação", ano_publicacao=1951, genero_id=g1.id, autor_id=a1.id),
    Livro(titulo="Eu, Robô", ano_publicacao=1950, genero_id=g1.id, autor_id=a1.id),
    Livro(titulo="Dom Casmurro", ano_publicacao=1899, disponivel=False, genero_id=g2.id, autor_id=a2.id),
    Livro(titulo="Memórias Póstumas", ano_publicacao=1881, genero_id=g2.id, autor_id=a2.id),
    Livro(titulo="O Iluminado", ano_publicacao=1977, genero_id=g3.id, autor_id=a3.id),
]
for l in livros:
    db.add(l)
db.commit()
print(f" {len(livros)} livros inseridos!")

todos = db.query(Livro).all()
for l in todos:
    print(f" [{l.id}] {l.titulo} ({l.ano_publicacao}) | Disponível: {l.disponivel}")

=======

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
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
db.close()