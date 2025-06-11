# declaração de variáveis
nome = input("Iforme seu nome: ")
idade = int(input("Informe sua idade: "))

# ternario
result = "é maior de idade." if idade >= 18 else "é menor de idade."

# saída
print(f"{nome} {result}")