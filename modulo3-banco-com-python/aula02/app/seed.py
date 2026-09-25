from app.database import SessionLocal
from app.models import Departamento, Cargo, Funcionario

def popular_banco():
    db = SessionLocal() # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])

        db.add_all([
          Funcionario(nome='Roberto Freitas', email='roberto.freitas@gmail.com', telefone='(11) 997664-6612', salario=5700.00, ativo=True),
          Funcionario(nome='Marisa Santos', email='marisa.santos@gmail.com', telefone='(21) 99051-0065', salario=4900.00, ativo=True),
          Funcionario(nome='Flávio Correia', email='flavio.correia@gmail.com', telefone='(44) 99034-5271', salario=4200.00, ativo=True),
          Funcionario(nome='Diantha Sousa', email='diantha.sousa@gmail.com', telefone='(31) 99643-8820', salario=6300.00, ativo=True),
        ])

        db.commit() # confirmar tudo no banco de uma vez
        print('Banco preenchido com sucesso')

    except Exception as e:
        db.rollback() # desfazer tudo se der erro
        print(f'Erro: {e}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()