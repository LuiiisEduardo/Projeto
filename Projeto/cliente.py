import socket 

def requisicao_cliente():
    lista_dia = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    lista_mes = ['1','2','3','4','5','6','7','8','9','10','11','12']
    ip = ''
    port = 7000 
    addr = ((ip,port)) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    client_socket.connect(addr) 
    print ("Escolha o número da operação que você deseja realizar")
    print ("1: Gás\n2: Temperatura\n3: Umidade\n4: Todos os dados")
    mensagem = input("Escolha uma opção:") 

    if (mensagem == '1' or mensagem == '2' or mensagem == '3' or mensagem == '4'):
        print ("Digite a data na ordem pedida")
        mensagem2 = input("Digite o dia:")
        if (mensagem2 in lista_dia or mensagem2 == ''):
            mensagem3 = input("Digite o mês:")
            if (mensagem3 in lista_mes or mensagem3 == ''):
                    mensagem4 = input("Digite o ano:")
            else:
                print("Mês inválido!")     
        else:
            print ("Dia inválido!")    
    else:
        print ("Operação escolhida inválida!")      
        
        
    data_pedida = "{}/{}/{}".format(mensagem2, mensagem3, mensagem4)

    client_socket.send(mensagem.encode())
    print ("mensagem enviada")
    client_socket.send(data_pedida.encode()) 
    print ("Data enviada")

    recebe = client_socket.recv(10000000).decode("UTF-8")
    print (recebe)
    if (recebe == "A data não existe no banco de dados!"):
        print ("Conexão encerrada!")
    else:
        
        nome_arquivo = input("Digite o nome do arquivo:")+".json"
        while (nome_arquivo == ''+'.json'):
            nome_arquivo = input("Por favor, digite o nome do arquivo:")+".json"
        else:
            fyle = open("{}".format(nome_arquivo), "w+")
            fyle.write(recebe)
            fyle.close()
            print ("Arquivo com os dados recebido!")
            client_socket.close()

try:
    requisicao_cliente()
except:
    print ("Conexão encerrada!")    