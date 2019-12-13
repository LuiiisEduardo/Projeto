# Projeto
Projeto final Programção para redes



Itens necessários:
1 Arduíno UNO
1 Protoboard
1 Buzzer
1 Sensor de gás MQ02
1 sensor de Umidade e Temperatura (DHT11)

Software necessário:
Arduíno IDLE (disponível no site: https://www.arduino.cc/en/main/software#).
Fritzing (A versão gratuíta estará disponível nos arquivos disponibilizados).
PgAdmin4

Importações necessárias para o uso correto dos programas:

- Fazer o download da biblioteca do DHT11 no site: https://blogmasterwalkershop.com.br/arduino/como-usar-com-arduino-sensor-de-umidade-e-temperatura-dht11/ e importar para dentro do IDLE do arduíno.
- No terminal, fazer o download das bibliotecas necessárias para o funcionamento dos programas python:

1 - Digite os seguintes comandos no terminal:

pip install serial
pip install pyserial
pip install psycopg2
Obs: Caso o pip não esteja instalado na máquina, digite no terminal " apt-get install python-pip "

Feito esses passos, agora é o momento de fazer o projeto funcionar:

2 - Vá até a pasta dos arquivos e realize o download da mesma.

3 - Abra a foto (Projeto_final.PNG) de demonstração da montagem dos sensores no arduíno e monte o equipamento.

4 - Após a montagem do equipamento, pegue o arquivo "cliente.py" e coloque em um diretório separado dos demais arquivos.

5 - Abra o software do Arduíno e abra o arquivo "Projeto_Final.ino" e grave o código na placa.

6 - Abra 4 terminais.

7 - No primeiro terminal, coloque para executar o arquivo "requisicao_db.py" com o seguinte comando:
	python3 requisicao_db.py
	7.1 - O arquivo "requisicao_db.py" estará criando o banco de dados.

8 - No segundo terminal, coloque para executar o arquivo "Sensores_Projeto_Final.py" com o seguinte comando:
	python3 Sensores_Projeto_Final.py
	8.1 - O arquivo "Sensores_Projeto_Final.py" estará capturando os dados dos sensores do arduíno e salvando no banco de dados.

9 - No terceiro terminal, coloque para executar o arquivo "servidor.py" com o seguinte comando:
	python3 servidor.py
	9.1 - O arquivo "servidor.py" é o servidor que irá esperar uma conexão de um cliente para enviar as informações guardadas no banco de dados.

10 - No quarto terminal, coloque para executar o arquivo "cliente.py" com o seguinte comando:
	python3 cliente.py
	10.1 - O arquivo "cliente.py" é o cliente que irá fazer as requisições do servidor e salvará os dados recebidos em um arquivo ".json".

