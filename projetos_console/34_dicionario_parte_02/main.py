# dicionário
pessoa = {
    'nome': "Fulano de Tal",
    'idade': 29,
    'email': "fulanodetal@gmail.com",
    'profissão': "DBA"
}

#exibir os valores
print(f"Nome: {pessoa.get('nome')}")
print(f"Idade: {pessoa.get('idade')}")
print(f"E-mail: {pessoa.get('email')}")
print(f"Profissão: {pessoa.get('profissão')}")
print(f"Gênero: {pessoa.get('genero')}")