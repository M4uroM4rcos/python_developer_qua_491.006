# dicionario
usuario = {
    'nome': "Mauro Marcos",
    'idade': 39,
    'email': "mauro@gmail.com",
    'profissão': "programaador"
}

# exibe os valores do dicionario
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")