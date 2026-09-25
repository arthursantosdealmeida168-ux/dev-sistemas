from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from app.routers import usuarios 

app = FastAPI(
    title='API de Cadastro - SENAI',
=======
from app.routers import usuarios

app = FastAPI(
    tile='API de Cadastro - SENAI',
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
    version='0.3.0'
)

app.add_middleware(
    CORSMiddleware,
<<<<<<< HEAD
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
=======
    allow_origins=["*"],  # ou seus origens configuradas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
)

# Registrar o router - inclui todas as rotas de usuarios.py
app.include_router(usuarios.router)

# Rota raiz permanece aqui
<<<<<<< HEAD
@app.get('/', tags=['Geral'])
=======
app.get('/', tags=['Geral'])
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
def raiz():
    return {'status': 'online', 'versão': '0.3.0'}