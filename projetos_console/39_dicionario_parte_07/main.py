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

#'Informe a chave que deseja excluir
chave = input("Informe a chave que deseja excluir: ").lower().strip()

# verificar se a chave existe
if chave in usuario:
    del usuario[chave]
else:
    print("Chave inválida.")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")