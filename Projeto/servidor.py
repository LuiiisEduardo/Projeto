import socket 
import psycopg2
from datetime import datetime

host = '' 
port = 7000 
addr = (host, port) 

def servidor():
    while True:
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        serv_socket.bind(addr) 
        serv_socket.listen(10) 
        print ('Aguardando conexao') 
        con, cliente = serv_socket.accept() 
        print ('Conectado' )
        print ("Aguardando solicitação:") 
        recebe = con.recv(1024).decode("UTF-8")
        recebe2 = con.recv(1024).decode("UTF-8")
        print ("Mensagem recebida:", recebe)
        print ("Data recebida:", recebe2) 
        
        now = datetime.now()
        data = "{}/{}/{}".format(now.day,now.month,now.year)
        
        if (recebe == '1' and recebe2 == '//' ):
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(data))
            gas_dados = cursor.fetchall()
            arquivo = open("gas_dados.json", "w")
            for dados in gas_dados:
                gas_dic =  {'Gás':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                print (gas_dic)
                print ("")
                arquivo.write(str(gas_dic))
                arquivo.write("\n")
            conexao.close()
            arquivo.close()
            enviar_arquivo = open("gas_dados.json", 'rb')
            kar = enviar_arquivo.read(10000000000)
            con.send(kar)   
            print ("Arquivo foi enviado!")
            enviar_arquivo.close()
            serv_socket.close()

        if (recebe == '1'):
            contador_gas = 0
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            #cursor.execute("SELECT * FROM dados_iot where data='{}'".format(data))
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(recebe2))
            gas_dados = cursor.fetchall()
            for data in gas_dados:
                contador_gas +=1
            if contador_gas == 0:
                print ("A data requisitada não existe no banco de dados!")
                con.send("A data não existe no banco de dados!".encode())
            else:    
                arquivo = open("gas_dados.json", "w")
                for dados in gas_dados:
                    gas_dic =  {'Gás':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                    print (gas_dic)
                    print ("")
                    arquivo.write(str(gas_dic))
                    arquivo.write("\n")
                conexao.close()
                arquivo.close()
                enviar_arquivo = open("gas_dados.json", 'rb')
                kar = enviar_arquivo.read(10000000000)
                con.send(kar)   
                print ("Arquivo foi enviado!")
                enviar_arquivo.close()
                serv_socket.close()

        if (recebe == '2' and recebe2 == '//'):
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(data))
            temperatura_dados = cursor.fetchall()
            arquivo = open("temperatura_dados.json", "w")
            for dados in temperatura_dados:
                temperatura_dic = {'Temperatura':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                print (temperatura_dic)
                print ("")
                arquivo.write(str(temperatura_dic))
                arquivo.write("\n")
            conexao.close()    
            arquivo.close()
            enviar_arquivo = open("temperatura_dados.json", 'rb')
            kar = enviar_arquivo.read(10000000000)
            con.send(kar)   

            print ("Arquivo foi enviado!")
            enviar_arquivo.close()
            serv_socket.close()

        if (recebe == '2'):
            contador_temperatura = 0
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(recebe2))
            temperatura_dados = cursor.fetchall()
            for data in temperatura_dados:
                contador_temperatura += 1
            if contador_temperatura == 0:
                print ("A data requisitada não existe no banco de dados!")
                con.send("A data não existe no banco de dados!".encode())
            else:    
                arquivo = open("temperatura_dados.json", "w")
                for dados in temperatura_dados:
                    temperatura_dic = {'Temperatura':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                    print (temperatura_dic)
                    print ("")
                    arquivo.write(str(temperatura_dic))
                    arquivo.write("\n")
                conexao.close()    
                arquivo.close()
                enviar_arquivo = open("temperatura_dados.json", 'rb')
                kar = enviar_arquivo.read(10000000000)
                con.send(kar)   

                print ("Arquivo foi enviado!")
                enviar_arquivo.close()
                serv_socket.close()

        if (recebe == '3' and recebe2 == '//'):
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(data))
            umidade_dados = cursor.fetchall()
            arquivo = open("umidade_dados.json", "w")
            for dados in umidade_dados:
                umidade_dic = {'Umidade':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                print (umidade_dic)
                print ("")
                arquivo.write(str(umidade_dic))
                arquivo.write("\n")
            conexao.close()
            arquivo.close()
            enviar_arquivo = open("umidade_dados.json", 'rb')
            kar = enviar_arquivo.read(10000000000)
            con.send(kar)   

            print ("Arquivo foi enviado!")
            enviar_arquivo.close()
            serv_socket.close()

        if (recebe == '3'):
            contador_umidade = 0
            conexao = psycopg2.connect(
                dbname='projeto',
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(recebe2))
            umidade_dados = cursor.fetchall()
            for data in umidade_dados:
                contador_umidade +=1
            if (contador_umidade == 0):
                print ()
                con.send("A data não existe no banco de dados!".encode())
            else:        
                arquivo = open("umidade_dados.json", "w")
                for dados in umidade_dados:
                    umidade_dic = {'Umidade':dados[0], 'Data':dados[3], 'Hora':dados[4]}
                    print (umidade_dic)
                    print ("")
                    arquivo.write(str(umidade_dic))
                    arquivo.write("\n")
                conexao.close()
                arquivo.close()
                enviar_arquivo = open("umidade_dados.json", 'rb')
                kar = enviar_arquivo.read(10000000000)
                con.send(kar)   

                print ("Arquivo foi enviado!")
                enviar_arquivo.close()
                serv_socket.close()


        if (recebe == '4' and recebe2 == '//'):
            conexao = psycopg2.connect(
                dbname='projeto', 
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(data))
            requisicao_dados = cursor.fetchall()
            arquivo = open("dados_completos.json", "w")
            for dados in requisicao_dados:
                dados_dic= {'Gas':dados[0], 'Temperatura':dados[1], 'Umidade':dados[2], 'Data':dados[3], 'Hora':dados[4]}
                print (dados_dic)
                print ("")
                arquivo.write(str(dados_dic))
                arquivo.write("\n")
            conexao.close()
            arquivo.close()
            enviar_arquivo = open("dados_completos.json", 'rb')
            kar = enviar_arquivo.read(10000000)
            con.send(kar)   

            print ("Arquivo foi enviado!")
            enviar_arquivo.close()
            serv_socket.close()

        if (recebe == '4'):
            contador_dados = 0
            conexao = psycopg2.connect(
                dbname='projeto', 
                user='postgres', 
                host='localhost', 
                password='admin')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM dados_iot where data='{}'".format(recebe2))
            requisicao_dados = cursor.fetchall()
            for data in requisicao_dados:
                contador_dados += 1
            if (contador_dados == 0):
                print ("A data requisitada não existe no banco de dados!")
                con.send("A data não existe no banco de dados!".encode())
            else:    
                arquivo = open("dados_completos.json", "w")
                for dados in requisicao_dados:
                    dados_dic= {'Gas':dados[0], 'Temperatura':dados[1], 'Umidade':dados[2], 'Data':dados[3], 'Hora':dados[4]}
                    print (dados_dic)
                    print ("")
                    arquivo.write(str(dados_dic))
                    arquivo.write("\n")
                conexao.close()
                arquivo.close()
                enviar_arquivo = open("dados_completos.json", 'rb')
                kar = enviar_arquivo.read(10000000)
                con.send(kar)   

                print ("Arquivo foi enviado!")
                enviar_arquivo.close()
                serv_socket.close()    

try:
    servidor()
except:
    print ("Conexão perdida!")               
    
        