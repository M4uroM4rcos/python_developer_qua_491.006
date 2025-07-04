import json
import os

usuarios = []
novo_arquivo = ""

while True:
    usuario = {}
    print("1 - Criar novo arquivo JSON (usuário irá informar o diretório).")
    print("2 - Abrir arquivo JSON (usuário irá informar o diretório).")
    print("3 - Cadastrar novo usuário em um JSON.")
    print("4 - Listar todos os usuários de um arquivo JSON.")
    print("5 - Pesquisar usuário através do valor de uma chave em um arquivo JSON.")
    print("6 - Alterar dados de um usuário em um arquivo JSON.")
    print("7 - Deletar usuário de um arquivo JSON.")
    print("8 - Sair do programa.")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

            with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(f"{'-'*20} DADOS {'-'*20}\n")
            for dado in dados:
                for chave in dado:
                    print(f"{chave.capitalize()}: {dado.get(chave)}")
            print("-"*47)

        case "2":
            if not novo_arquivo:
                novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            
            with open(f"{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(f"{'-'*20} USUÁRIOS {'-'*20}\n")
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
            print(f"{'-'*50}")

        case "3":
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['data_nasc'] = input("Informe a data de nascimento: ").strip()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['email'] = input("Informe o e-mail: ").strip().lower()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['filme_favorito'] = input("Informe o filme favorito: ").strip().title()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuário cadastrado com sucesso.")
            continue
        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case "7":
            ...
        case "8":
            print("Programa encerrado com sucesso!")
            break
        case _:
            print("Opção errada")
            continue