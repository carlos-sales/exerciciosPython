nome = str(input('Digite o nome: ')).strip()
print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Qtd sem espaço: {}'.format(len(nome)-nome.count(' ')))
print('Qtd primeiro nome: {}'.format(len(nome.split()[0])))
print('Qtd primeiro nome: {}'.format(nome.find(' ')))
