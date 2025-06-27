# dicionario
usuario = {
    'nome': "Mauro Marcos",
    'idade': 39,
    'email': "mauro@gmail.com",
    'profissão': "programaador"
}

for chave in usuario:
    print(f'{chave.capitalize()}: {usuario.get(chave)}')
print("-"*40)
# alterar uma chave do dicionario
chave = input("Informe a chave que deseja alterar: ").lower().strip()

# usuario informa o valor da chave
if chave in usuario:
    usuario[chave] = input(f'Informe o valor de {chave}: ').strip()
else:
    print("Chave inexistente.")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")