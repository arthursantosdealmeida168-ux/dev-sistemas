# API Loja de Games

API RESTful para gerenciar o catálogo de uma loja de games; plataformas, jogos e avaliações dos clientes.

---

## Tecnologias utilizadas
-Python 3
-FastAPI
-SQLAlchemy
-Pydantic
-Uvicorn

---

## Como instalar e executar
1. Clone o repositório e entre na pasta do projeto:
```
git clone https://github.com/arthursantosdealmeida168-ux/dev-sistemas.git
cd loja-games
```
2. Crie e ative o ambiente virtual(venv)
```
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências:
```
pip install fastapi uvicorn sqlalchemy
```

4. Execute o servido:
```
uvicorn main:app --reload
```

5. Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

---
## Rotas da API
| Método | Rotas | O que faz |
| --- | --- | --- |
| GET | '/plataforma/' | Lista todas as plataformas |
| POST | '/plataforma' | Cadastra uma nova plataforma |
| GET | '/jogos/' | Lista todos os jogos |
| POST | '/jogos{id}' | Busca um jogo pelo ID |

---

## Autor
Arthur santos de almeida - Desenvolvimento de Sistemas - SENAI - DF