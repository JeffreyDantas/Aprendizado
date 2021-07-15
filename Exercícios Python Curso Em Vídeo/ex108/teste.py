import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}!')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}!')
print(f'{moeda.moeda(p)} com aumento de 10%, fica {moeda.moeda(moeda.aumentar(p, 10))}!')
print(f'{moeda.moeda(p)} menos 10%, fica {moeda.moeda(moeda.diminuir(p, 10))}!')