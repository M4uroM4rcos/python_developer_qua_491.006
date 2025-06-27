chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")
usuario = {
    chaves[0]: "Mauro Marcos",
    chaves[1]: 39,
    chaves[2]: "mauro@gmail.com",
    chaves[3]: "(61) 98765-4321",
    chaves[4]: "Estudante"
}

for chave in chaves:
    print(f'{chave}: {usuario.get(chave)}')