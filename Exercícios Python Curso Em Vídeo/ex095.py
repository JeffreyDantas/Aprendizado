#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range (tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp in 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
     print(f'{k:>3} ',end='')
     for d in v.values():
        print(f'{str(d):<15}',end='')
     print()
print('-'*40)
while True:
    escolha = int(input('Mostrar dados de qual jogador?(999 parar): '))
    if escolha == 999:
        break
    if escolha >= len(time):
        print(f'ERRO! Não existe jogador com código {escolha}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[escolha]["nome"]}:')
        for i, g in enumerate(time[escolha]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')