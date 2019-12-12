import psycopg2

def criar_Banco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        host='localhost', 
        password='admin')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cursor.execute("CREATE DATABASE projeto")
    conexao.commit()
    conexao.close()
    print ("Banco de Dados criado com sucesso!")

def criar_Tabela():
    conexao = psycopg2.connect(
        dbname='projeto', 
        user='postgres', 
        host='localhost', 
        password='admin')
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE Dados_IoT (Gas VARCHAR (50), Temperatura VARCHAR (50), Umidade VARCHAR (50), Data VARCHAR (50), Hora VARCHAR (50))")
    conexao.commit()
    conexao.close()
    print ("Tabela criada com sucesso!")

try:
    criar_Banco()
    criar_Tabela()
except:
    print ("Banco e tabelas já criados!")