import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}!')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}!')
print(f'{moeda.moeda(p)} com aumento de 10%, fica {moeda.aumentar(p, 10, True)}!')
print(f'{moeda.moeda(p)} menos 10%, fica {moeda.diminuir(p, 10, True)}!')