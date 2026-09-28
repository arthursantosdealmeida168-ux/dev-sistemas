from app.database import engine, Base, SessionLocal
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario, listar_funcionarios, buscar_funcionario, atualizar_funcionario, desativar_funcionario
from app.crud import criar_departamento, listar_departamentis, atualizar_departamento, destativar_departamento

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
# 1 CREATE
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Jorge simas', 'jorge@gmail.com', '(66) 99085-8321', 3300.0)
    print(f'Criado: {novo}')

# 2 READ
    todos = listar_funcionarios(db)
    print(f'Total: {len(todos)} funcionarios')
    for funcionario in todos:
        print(f' {funcionario.nome} - R${funcionario.salario}')

        um = buscar_funcionario(db,1)
        if um:
            print(f'\nFuncionario 1: {um.nome}')

# 3 UPDATE
    atualizado = atualizar_funcionario(db, 1, salario=5500.0)
    print(f'{atualizado.nome}: R$ {atualizado.salario}')

# 4 DELETE
    desativado = desativar_funcionario(db, 3)
    print(f'{desativado.nome}: ativo={desativado.ativo}')

    ativo = listar_funcionarios(db, apenas_ativos=True)
    print(f'Ativos restantes: {len(ativo)}')

finally:
    db.close()

db = SessionLocal()
try:
    # Criar
    novo = criar_departamento(db, 'Jurídico', 'JUR')
    print(f'Criado: {novo.nome} ({novo.sigla})')

    # Listar
    todos = listar_departamentis(db)
    print(f'Total: {len(todos)} departamentos')

    # Atualizar
    atualizado = atualizar_departamento(db, novo.id, 'Jurídico e Compliance')
    print(f'Atualizado: {atualizado.nome}')

    # Desativar
    desativado = destativar_departamento(db, novo.id)
    print(f'Desativado: {desativado.nome} - ativo={desativado.ativo}')

finally:
    db.close()