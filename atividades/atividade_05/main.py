# importa biblioteca
import os
import datetime
from datetime import date

nome = input("Informe seu Nome: ").title().strip()
idade = int(input("Informe sua idade: "))

hoje = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

while True:
    # menu
    print(f"{'-'*20}🐍 CINEMA🐍 {'-'*20}\n")
    print("Sala 1: A Roda Quadrada - livre")
    print("Sala 2: A Volta dos Que Não Foram - 12 anos")
    print("Sala 3: Poeira em Alto Mar - 14 anos")
    print("Sala 4: As Tranças do Rei Careca - 16 anos")
    print("Sala 5: A Vingança do Peixe Frito - 18 anos")
    print("Digite 6 para concluir a operação.")
    sala = input("Informe sua sala: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    try:
        
        match sala:
            case "1":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Sala: 1, Filme: A Roda Quadrada.")
                print(f"Favor se direcione a sala: 1 Sr. {nome}")
                print(f"Hora da compra: {hora}, na data: {hoje}")
                continue
        
            case "2":
                idade >= 12 or idade < 14
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Sala: 2, Filme: A Volta dos Que Não Foram.")
                print(f"Favor se direcione a sala: 2 Sr. {nome}")
                print(f"Hora da compra: {hora}, na data: {hoje}")
                continue

            case "3":
                idade >= 14 or idade < 16
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Sala: 3, Filme: Poeira em Alto Mar.")
                print(f"Favor se direcione a sala: 3 Sr. {nome}")
                print(f"Hora da compra: {hora}, na data: {hoje}")
                continue

            case "4":
                idade >= 16 or idade < 18
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Sala: 4, As Tranças do Rei Careca.")
                print(f"Favor se direcione a sala: 4 Sr. {nome}")
                print(f"Hora da compra: {hora}, na data: {hoje}")
                continue

            case "5":
                idade >= 18
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Sala: 5, Filme: A Vingaça do Peixe Frito.")
                print(f"Favor se direcione a sala: 5 Sr. {nome}")
                print(f"Hora da compra: {hora}, na data: {hoje}")
                continue

            case "6":
                print("Programa encerrado.")
                break

            case _:
                print("Sala inexistente. Favor escolher outra sala.")
                continue

    except Exception as e:
        print(f"Não foi possível comprar o ingresso. {e}.")
        continue