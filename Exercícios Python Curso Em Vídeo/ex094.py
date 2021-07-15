#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em uma lista.
#No final, mostre:
#A)Quantas pessoas foram cadastradas.
#B)A Média de idade do grupo.
#C)Uma lista com todas as mulheres.
#D)Uma lista com todas as pessoas com idade acima da média.
galera = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo {len(galera)} pessoas foram cadastradas!')
média = soma / len(galera)
print(f'A Média de idade é de {média:5.2f} anos!')
print('As mulheres cadastradas são ',end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas com idade acima da média')
for p in galera:
    if p['idade'] >= média:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<<<ENCERRADO>>>')