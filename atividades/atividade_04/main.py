import time
import datetime
import os

while True:
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    print(hora_formatada)
    time.sleep(1)
    os.system("cls")