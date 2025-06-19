import calendar

def exibir_calendario(ano):
  """Exibe o calendário completo de um ano."""
  print(calendar.calendar(ano))

def exibir_calendario_mensal(ano, mes):
  """Exibe o calendário de um mês específico de um ano."""
  print(calendar.month(ano, mes))

# Solicita o ano ao usuário
ano_desejado = int(input("Digite o ano: "))

# Exibe o calendário anual
exibir_calendario(ano_desejado)

# Solicita o mês ao usuário
mes_desejado = int(input("Digite o mês (1-12): "))

# Exibe o calendário mensal
exibir_calendario_mensal(ano_desejado, mes_desejado)