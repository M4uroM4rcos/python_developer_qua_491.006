# importa biblioteca
import math
import os

while True:
    # menu
    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Calcular área de um circulo")
    print("2 - Calcular área de uma circuferência")
    print("3 - Sair do programa")
    opcao = input("Informe sua opção: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    try:
        if opcao == "1" or opcao == "2":
            raio = float(input("informe o valor do raio: ").replace(",", "."))
        else:
            ...

        match opcao:
            case "1":
                area = math.pi * (raio ** 2)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Área do circulo: {area:.3f}")
                continue
        
            case "2":
                circuferencia = 2 * math.pi * raio
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Tamanho da circuferência: {circuferencia:.3f}")
                continue

            case "3":
                print("Programa encerrado.")
                break

            case _:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Opção inválida.")
                continue

    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
        continue