# Atividade
''' Crie um CRUD, ou seja, um programa que:
- Cadastre
- Liste
- Altere
- Exclua

O programa deverá cadastrar pessoas com os seguintes dados:
Nome, CPF, E-mail, Telefone, Data de Nascimento, Gênero.'''
# NOTE: O usuário poderá cadastrar quantas pessoas quiser.
# NOTE: O progra deverá fornecer no menu com a opçoes: cadastrar, listar, alterar, excluir e sair do programa.

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
        print("0 - Sair do programa")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar todos os usuários")
        print("3 - Alterar os dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Sortear usuário")
        
        opcao = input("\nInforme a opção desejada: ")

        match opcao:
            case "0":
                print("\nPrograma encerrado!\n")
                break
            
            case "1":

                usuario['nome'] = input("Informe o nome do usuário: ")
                usuario['email'] = input("Informe o e-mail do usuário: ")
                usuario['cpf'] = input("Informe o CPF do usuário: ")
                usuario['telefone'] = input("Informe o Telefone da usuario: ")
                usuario['data_nasc'] = input("Informe a data de nascimento: ")
                usuario['genero'] = input("Informe o gênero do usuario: ")
                                
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
                    print("\n")
                continue

            case "3":
                os.system("cls")
                posicao = int(input("Informe a posição do usuário que deseja alterar: "))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print("\n")
                    dado = input("Informe o nome da chave que deseja alterar: ")
                    if lista[posicao][dado]:
                        lista[posicao][dado] = input(f"Informe o valor de {dado}: ")
                        os.system("cls")
                        print("Dados alterados com sucesso\n")
                    else:
                        print("Chave inválida!")
                else:
                    print("Posição inválida!")
                    continue
            case "4":
                os.system("cls")
                posicao = int(input("Informe a posição do usuario que deseja excluir: "))
                if (lista[posicao]):
                    del(lista[posicao])
                    os.system("cls")
                    print("Usuário ecluido com sucesso!")
                else:
                    print("Não foi possivél excluir o usuário!")
                continue
            case "5":
                for nome in usuario:
                    nome_sorteado = random.choice(usuario(nome))
                    print(f"O nome sorteado foi: {nome_sorteado}")
            case "_":
                print("Opção inválida.")
                continue

except Exception as e:
    print(f"Não foi possivel executar a operação. {e}.")