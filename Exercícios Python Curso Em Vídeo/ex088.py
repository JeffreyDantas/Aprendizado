#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
quant = int(input('Quantos jogos você quer sortear? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print(f'SORTEANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print('-='*5, 'BOA SORTE!', '-='*5)
