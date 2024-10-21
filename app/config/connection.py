from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Parametros de conexao com MySQL

db_user = "user"
db_password = "user_password"
#localhost = minha maquina
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

#URL DE CONEXAO PARA BD MySQL
#DATABASE_URL = f"mysql+pymysql://usuario:senha@host:porta/nome_bd"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def git_db():
    db = Session() # Cria uma sessão para ações no banco de dados.
    try:
        yield db # Caso a sessão realize todas as tarefas, salva a operação.
        db.commit()
    except Exception as erro:
        db.rollback() # Desfaz todas alterações em caso de erro em alguma operação.
        raise erro # Lança uma exceção.
    finally:
        db.close() #Fecha a sessão com o bando de dados.
