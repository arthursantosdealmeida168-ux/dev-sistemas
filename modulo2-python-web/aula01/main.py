<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
# main.py -- Primeira API com FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
title='API de Cadastro -- SENAI',
description='Primeira API do curso de Desenvolvimento de Sistemas',
version='0.1.0'
)

app.add_middleware(
CORSMiddleware,
allow_origins=['*'],
# em producao, especificar o dominio do front
allow_methods=['*'],
allow_headers=['*'],
<<<<<<< HEAD
=======
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Criar a instancia da aplicação
app = FastAPI(
    title='API de Cadastro -- SENAI',
    description='Primeira API do curso de DS',
    version='0.1.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # Em produção, especificar o dominio do front
    allow_methods=['*'],
    allow_headers=['*'],
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
)

# Rota raiz -- GET /
@app.get('/')
def raiz():
    return {'mensagem': 'API funcionando!', 'versao': '0.1.0'}

# Rota de status -- GET /status
@app.get('/status')
def status():
    return {'status': 'online', 'servico': 'API SENAI'}

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
# Lista simulada de usuarios -- substitui o banco por enquanto
usuarios_db = [
    {'id': 1, 'nome': 'Carlos Silva', 'cargo': 'Desenvolvedor', 'ativo': True},
    {'id': 2, 'nome': 'Ana Lima', 'cargo': 'Designer', 'ativo': True},
    {'id': 3, 'nome': 'Bruno Costa', 'cargo': 'QA', 'ativo': False},
]

# GET /usuarios -- retorna todos os usuarios
<<<<<<< HEAD
=======
=======
# Lista simulada de usuarios --  substitui o banco por enquanto
usuarios_db = [
    {'id': 1, 'nome': 'Max Muller', 'cargo': 'DEV', 'ativo': True},
    {'id': 2, 'nome': 'Alice Lima', 'cargo': 'Design', 'ativo': True},
    {'id': 3, 'nome': 'Carlos Silva', 'cargo': 'QA', 'ativo': False},
]

# GET /usuarios - retorna todos os usuarios
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
@app.get('/usuarios')
def listar_usuarios():
    return usuarios_db

<<<<<<< HEAD
# GET /usuarios/busca?nome=carlos -- query parameter
# O nome vem da URL depois do ?
=======
<<<<<<< HEAD
# GET /usuarios/busca?nome=carlos -- query parameter
# O nome vem da URL depois do ?
=======
# GET /usuarios/(id) - retorna um usuario pelo ID
# O (id) é um path parameter - FastAPI extrai da URL automaticamente


>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
@app.get('/usuarios/busca')
def buscar_por_nome(nome: str = ''):
    if not nome:
        return usuarios_db
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    filtrados = [u for u in usuarios_db if nome.lower() in u['nome'].lower()]
    return filtrados

# GET /usuarios/ativos -- retorna apenas usuarios ativos
<<<<<<< HEAD
=======
=======
    filtrados = [u for u in usuarios_db if nome.lower() in u ['nome'].lower()]
    return filtrados



>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
@app.get('/usuarios/ativos')
def listar_ativos():
    return [u for u in usuarios_db if u['ativo']]

<<<<<<< HEAD
# GET /usuarios/inativos -- retorna apenas usuarios inativos
=======
<<<<<<< HEAD
# GET /usuarios/inativos -- retorna apenas usuarios inativos
=======
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
@app.get('/usuarios/inativos')
def listar_inativos():
    return [u for u in usuarios_db if not u['ativo']]

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
# GET /usuarios/cargo/{cargo} -- filtra pelo cargo (case-insensitive)
@app.get('/usuarios/cargo/{cargo}')
def buscar_por_cargo(cargo: str):
    return [
u for u in usuarios_db
if cargo.lower() in u['cargo'].lower()
]

# GET /info -- estatisticas gerais da API
@app.get('/info')
def info_geral():
    return {
'total_usuarios': len(usuarios_db),
'ativos': sum(1 for u in usuarios_db if u['ativo']),
'inativos': sum(1 for u in usuarios_db if not u['ativo']),
}

# GET /usuarios/{id} -- retorna um usuario pelo ID
# O {id} e um path parameter -- FastAPI extrai da URL automaticamente
<<<<<<< HEAD
=======
=======
@app.get('/usuarios/cargo/{cargo}')
def buscar_por_cargo(cargo: str):
    return [
        u for u in usuarios_db
        if cargo.lower() in u['cargo'].lower()
    ]

@app.get('/info')
def info_geral():
    return {
        'total_usuarios': len(usuarios_db),
        'ativos': sum(1 for u in usuarios_db if u['ativo']),
        'inativos': sum(1 for u in usuarios_db if not u['ativo']),
    }

# GET /usuarios/(id) - retorna um usuario pelo ID
# O (id) é um path parameter - FastAPI extrai da URL automaticamente
>>>>>>> 47da6c05f42bdfa75d0b70c1a0bf94f88c94c96e
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
@app.get('/usuarios/{usuario_id}')
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario['id'] == usuario_id:
            return usuario
    return {'erro': 'Usuario nao encontrado'}