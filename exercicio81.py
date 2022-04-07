item = []
while True:
    item.append(int(input('digite um item: ')))
    resp= str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(item)} elementos')
item.sort(reverse=True)
print(f'Item em ordem decrescente {item}')
if 5 in item:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista ')

