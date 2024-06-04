def ExibirMensagem(nome):
    print(f'Seja bem vindo {nome}')
    return f'Usuário logado: {nome}'

nome_usuario = input(' Digite o nome de usuário: ')
usuario = ExibirMensagem(nome_usuario)
print(usuario)