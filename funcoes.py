def ExibirMensagem(nome, mensagem="Seja bem vindo"):
    print(f'{mensagem} {nome}')
    return f'Usuário logado: {nome}'

nome_usuario = input(' Digite o nome de usuário: ')
msg = input(" Digite uma mensagem: ")
usuario = ExibirMensagem(nome_usuario, msg)
print(usuario)

print(50 * "_")

def ExibirMensagem(nome, mensagem="Seja bem vindo"):
    print(f'{mensagem} {nome}')
    return f'Usuário logado: {nome}'

nome_usuario = input(' Digite o nome de usuário: ')
msg = input(" Digite uma mensagem: ")
usuario = ExibirMensagem(nome_usuario, msg)
print(usuario)