# importar biblioteca
import os
import datetime
from datetime import date
import random

# Lista de dicionarios
lista = []

try:
    while True:
        usuario = {}

        print(f"{'='*20} CRUD COBRA {"="*20}")
        print("O quê deseja fazer?")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar todos os usuários")
        print("3 - Alterar os dados de um usuário")
        print("4 - Sortear usuário")
        print("5 - Excluir um usuário")
        print("6 - Sair do programa")
        
        opcao = input("\nInforme a opção desejada: ")

        match opcao:
            case "1":

                usuario['nome'] = input("Informe o nome do usuário: ")
                usuario['email'] = input("Informe o e-mail do usuário: ")
                usuario['cpf'] = input("Informe o CPF do usuário: ")
                usuario['telefone'] = input("Informe o Telefone da usuario: ")
                usuario['data_nasc'] = input("Informe a data de nascimento: ")
                usuario['genero'] = input("Informe o gênero do usuario: ")
                usuario['data do cadastro'] = date.today().strftime("%d/%m/%Y")
                usuario['hora do cadastro'] = datetime.datetime.now().strftime("%H:%M:%S")
                                
                lista.append(usuario)
                os.system('cls')
                print(f"{usuario.get('nome')} cadastrado com sucesso!\n")
                continue
                
            case "2":
                os.system("cls")
                for i in range(len(lista)):
                    print(f"Posição: {i}")
                    for chave in lista[i]:
                        print(f"{chave.title()}: {lista[i].get(chave)}.")
                    print(f"{"-"*25}\n")
                continue

            case "3":
                os.system("cls")
                posicao = int(input("Informe a posição do usuário que deseja alterar: "))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print("\n")
                    while True:
                        dado = input("Informe o nome da chave que deseja alterar: ")
                        if lista[posicao][dado]:
                            lista[posicao][dado] = input(f"Informe o valor de {dado}: ")
                            os.system("cls")
                            print("Dados alterados com sucesso\n")
                        else:
                            print("Chave inválida!")
                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir == "s" or prosseguir == "n":
                                break
                            else:
                                continue
                        match prosseguir:
                            case "s":
                                continue
                            case "n":
                                break
                else:
                    print("Posição inválida!")
                    continue

            case "4":
                try:
                    i = random.randint(0, len(lista)-1)
                    print("Usuário sorteado:")
                    for nome in lista[1]:
                        print(f"{chave.capitalize()}: {lista[1].get(chave)}")
                except Exception as e:
                    print(f"Não foi possével sortear usuário. {e}")

            case "5":
                os.system("cls")
                posicao = int(input("Informe a posição do usuario que deseja excluir: "))
                if (lista[posicao]):
                    del(lista[posicao])
                    os.system("cls")
                    print("Usuário ecluido com sucesso!")
                else:
                    print("Não foi possivél excluir o usuário!")
                continue
            case "6":
                print("\nPrograma encerrado!\n")
                break
            
            case "_":
                print("Opção inválida.")
                continue

except Exception as e:
    print(f"Não foi possivel executar a operação. {e}.")