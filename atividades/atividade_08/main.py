# importar biblioteca
import os

# Apresentação
print(f"{"-"*20} Bem Vinda a escola Cobra {"-"*20}\n")

nome = input('Informe o nome do aluno: ')

notas = []

while True:
    print("1 - Informe uma nota de 0 a 10.")
    print("2 - Tirar a média e sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls")
    match opcao:
        case "1":
            try:
                nova_nota = float(input("Inserir a noova nota: ").replace(",", "."))
                if nova_nota >= 0 and nova_nota <= 10:
                    os.system("cls")
                    notas.append(nova_nota)
                    print("Nota inserida comseucesso!")
                else:
                    print("Nota inválida")
            except Exception as e:
                print(f"Não foi possivél calcular. {e}.")
            finally:
                continue
        case "2":
            try:
                media = sum(notas) / len(notas)
                print(f"Média: {media:.2f}")
                if media >= 7:
                    print(f'{nome} está aprovado.')
                elif media >= 5:
                    print(f'{nome} está de recuperação.')
                else:
                    print(f'{nome} está reprovado.')
            except Exception as e:
                print("Não foi possivél calcular a média.")
            finally:
                break
        case _:
            print("Opção invalida.")
            continue