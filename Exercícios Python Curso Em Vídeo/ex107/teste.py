import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}!')
print(f'O Dobro de R${p:.2f} é R${moeda.dobro(p):.2f}!')
print(f'R${p:.2f} com aumento de 10%, fica R${moeda.aumentar(p, 10):.2f}!')
print(f'R${p:.2f} menos 10%, fica R${moeda.diminuir(p, 10):.2f}!')