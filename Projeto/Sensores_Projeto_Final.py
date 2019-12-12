import time
import serial
from datetime import datetime
import psycopg2

conexao = serial.Serial("/dev/ttyUSB0", 9600)

def sensores():
    while True:
        now = datetime.now()
        data = "Data = {}/{}/{}".format(now.day,now.month,now.year)
        hora = "Hora = {}:{}:{}".format(now.hour,now.minute,now.second)
        data_db = "{}/{}/{}".format(now.day,now.month,now.year)
        hora_db = "{}:{}:{}".format(now.hour,now.minute,now.second)
        leitura_serial = conexao.readline()
        leitura_serial_str = str(leitura_serial)
        dados = leitura_serial_str[2:][:-5]
        gas_db = leitura_serial_str[7:][:5]
        umidade_db = leitura_serial_str[21:][:6]
        temperatura_db = leitura_serial_str[43:][:7]
        print (dados,data,hora)

        conexao2 = psycopg2.connect(
            dbname='projeto', 
            user='postgres', 
            host='localhost', 
            password='admin')
        cursor = conexao2.cursor()
        cursor.execute("INSERT INTO dados_iot(gas, temperatura, umidade, data, hora) VALUES ('{}','{}','{}','{}','{}')".format(gas_db,temperatura_db,umidade_db,data_db,hora_db))
        conexao2.commit()
        conexao2.close()
      
try:
    sensores() 
except:
    print ("Programa encerrado!")            