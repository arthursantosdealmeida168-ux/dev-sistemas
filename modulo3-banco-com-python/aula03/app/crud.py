from sqlalchemy.orm import Session
from app.models import Funcionario, Departamento

<<<<<<< HEAD
# CREATE - Criar um novo funcionário
def criar_funcionario(db: Session, nome: str, email: str, salario: float):
    # 1 Verificar se o email já existe
=======
def criar_funcionario(db: Session, nome: str, email: str, telefone:str, salario: float):
    # 1 Verifacar se o email ja existe
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    existe = db.query(Funcionario).filter(
        Funcionario.email == email
    ).first()

    if existe:
        raise ValueError(f'E-mail {email} já cadastrado')

    # 2 Criar o objeto
<<<<<<< HEAD
    novo = Funcionario(nome=nome, email=email, salario=salario)
=======
    novo = Funcionario(nome=nome, email=email, telefone=telefone, salario=salario)
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616

    # 3 Salvar no banco
    db.add(novo)
    db.commit()
<<<<<<< HEAD
    db.refresh(novo)  # busca o id pelo banco
    return novo

# READ - Listar funcionarios com cadastro ativo
=======
    db.refresh(novo) # busca o id pelo banco
    return novo

# READ - Buscar funcionarios com cadastro ativo
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
def listar_funcionarios(db: Session, apenas_ativos: bool=True):
    query = db.query(Funcionario)
    if apenas_ativos:
        query = query.filter(Funcionario.ativo == True)
        return query.order_by(Funcionario.nome).all()

<<<<<<< HEAD
# READ - Buscar funcionario pelo id
=======
# READ - Buscar funcionario pela id
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
def buscar_funcionario(db: Session, funcionario_id: int):
    return db.query(Funcionario).filter(
        Funcionario.id == funcionario_id
    ).first()    # Retorna None se não encontrar

<<<<<<< HEAD
# UPDATE - Atualizar o salário de um funcionário 
def atulizar_funcionario(
        db: Session, funcionario_id: int,
        nome: str = None, salario: float = None
):  
    func = buscar_funcionario(db, funcionario_id)

    if not func:
        raise ValueError(f'Funcionário {funcionario_id} não encontrado')
=======
# UPDATE -
def atualizar_funcionario(
        db: Session, funcionario_id: int,
        nome: str = None, salario: float = None
):
    func = buscar_funcionario(db, funcionario_id)

    if not func:
        raise ValueError(f'Funcionário {funcionario_id} não encotrado')
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616

    # Atualizar só os campos que foram enviados
    if nome is not None:
        func.nome = nome
    if salario is not None:
        func.salario = salario

    db.commit()       # confirma a alteração no banco
    db.refresh(func)  # sincronizar
    return func

<<<<<<< HEAD
# DELETE - Desativar o cadastro de um funcionário ativo para inativo
=======
# DELETE
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
def desativar_funcionario(db: Session, funcionario_id: int):
    func = buscar_funcionario(db, funcionario_id)

    if not func:
<<<<<<< HEAD
        raise ValueError(f'Funcionário {funcionario_id} não encontrado')
=======
        raise ValueError(f'funcionário {funcionario_id} não encontrado')
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616

    if not func.ativo:
        raise ValueError(f'Funcionário {funcionario_id} já está inativo')

<<<<<<< HEAD
    func.ativo = False  # Soft delete: só muda o campo
    db.commit()
    return func

# Atividade - CRUD de Departamentos 
def criar_departamento(db, nome, sigla):
    existe = db.query(Departamento).filter(Departamento.sigla == sigla).first()
    if existe: raise ValueError(f'Sigla {sigla} já cadastrada')
    novo = Departamento(nome=nome, sigla=sigla)
    db.add(novo); 
    db.commit(); 
    db.refresh(novo)
    return novo

def listar_departamentos(db):
    return db.query(Departamento).order_by(Departamento.nome).all()

def buscar_depto_por_id(db, depto_id):
    return db.query(Departamento).filter(Departamento.id == depto_id).first()

def atualizar_departamento(db, depto_id, nome):
    depto = buscar_depto_por_id(db, depto_id)
    if not depto: raise ValueError(f'Departamento {depto_id} não encontrado')
    depto.nome = nome; 
    db.commit(); 
    db.refresh(depto)
    return depto

def desativar_departamento(db, depto_id):
    depto = buscar_depto_por_id(db, depto_id)
    if not depto: raise ValueError(f'Departamento {depto_id} não encontrado')
    depto.ativo = False; 
=======
    func.ativo = False # Soft delete: só muda o campo
    db.commit()
    return func

# ATIVIDADE
def criar_departamento(db: Session, nome: str, sigla: str):
    # Verificar se a sigla já existe
    existe = db.query(Departamento).filter(
       Departamento.sigla == sigla    # modelo e campo e valor
    ).first() # sé não encontrar ele retorna ao valor none/nulo

    if existe:
        raise ValueError(f'Sigla {sigla} já cadastrada')
    novo = Departamento (nome=nome, sigla=sigla) # criar o objeto
    db.add(novo)      # adicionar à sessão
    db.commit()       # confirmar
    db.refresh(novo)
    return novo

def listar_departamentis(db: Session):
    return db.query(Departamento).order_by(Departamento.nome).all() # todos ordenados por nome

def buscar_depto_por_id(db: Session, depto_id: int):
    return db.query(Departamento).filter(
        Departamento.id == depto_id # qual campo?
    ).first()

def atualizar_departamento(db: Session, depto_id: int, nome: str):
    depto = buscar_depto_por_id(db, depto_id)

    if not depto:
        raise ValueError(f'Departamento {depto_id} não encontrado')

    depto.nome = nome
    db.commit()
    db.refresh(depto)
    return depto

def destativar_departamento(db: Session, depto_id: int):
    depto = buscar_depto_por_id(db, depto_id)

    if not depto:
        raise ValueError(f'Departamento {depto_id} não encotrado')
    depto.ativo = False # qual campo? qual valor para desativar?
>>>>>>> b70bcd867e29269b04eac9fd4616173b74b86616
    db.commit()
    return depto