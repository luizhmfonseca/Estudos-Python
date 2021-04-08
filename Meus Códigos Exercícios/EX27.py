n = str (input('Digite um nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome: {} '.format(nome[0]))
print('Seu último nome: {}'.format(nome[len(nome)-1])) # conta um nome a menos
print('Seu usuário de rede será {}'.format(nome[0]) + (nome[3]))