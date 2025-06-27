# dicionario
usuario = {
    'nome': "Mauro Marcos",
    'idade': 39,
    'email': "mauro@gmail.com"
}
# exibi dicionario
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adicionando nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")