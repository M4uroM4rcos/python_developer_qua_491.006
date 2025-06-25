# importar biblioteca
import os

# declarar lista
nomes = []

while True:
    # menu
    print("1 - Cadastre novo nome na lista")
    print("2 - Liste todos os nomes na lista")
    print("3 - Pesquise um nome na lista")
    print("4 - Altere um nome na lista")
    print("5 - Exclua um nome na lista")
    print("6 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                novo_nome = input("Informe novo nome: ").title().strip()
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")        
            except Exception as e:
                print(f'Não foi possivel inserir novo nome. {e}.')
            finally:
                continue
        case "2":
            try:
                for i in range(len(nomes)):
                    print(f"{i}: {nomes[1]}")
                print('-'*40)
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe nome a ser pesquisado: ").title().strip()
            os.system("cls" if os.name == "nt" else "clear")
            qtde = nomes.count(nome_pesquisado)
            print(f"{nome_pesquisado} foi encontrado {qtde} vezes.")
            continue
        case "4":
            try:
                i = int(input("Informe o indice a ser alterado: "))
                if i >= 0 and i < len(nomes):
                    nomes[1] = input("Informe o novo nome: ").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    print("Indice inválido.")
            except Exception as e:
                print(f'Não foi possivel alterar. {e}.')
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe o indice que deseja excluir: "))
                if i >= 0 and i < len(nomes):
                    del(nomes[i])
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Nome deletado com sucesso!")
                else:
                    print("Indice inválido.")
            except Exception as e:
                print(f'Não foi possivél excluir. {e}.')
            finally:
                continue
        case "6":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
            continue