# importação
import os

# Lista
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]

for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("-"*60)

try:
    i = int(input("Informe o índice que deseja separar:"))
    if i >= 0 and i < len(nomes):
        nome_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_isolado} separado com sucesso!")

        #Lista exibe os valores sem item isolado
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
        print("-"*60)
    else:
        print("Indice inválido!")

except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")