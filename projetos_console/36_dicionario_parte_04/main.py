# dicionario
usuario = dict(nome="Mauro Marcos", idade=39, email="mauro@gmail.com")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")