from datetime import datetime

# Obtém a data e hora atuais
agora = datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")
print(hora_formatada)

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")
print(data_formatada)