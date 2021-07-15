#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O Programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato!
dados = {}
totgols = 0
gols = []
dados['nome'] = str(input('Nome do Jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range (dados['partidas']):
    dados['gols'] = int(input(f'Quantos gols na partida {c}? '))
    totgols = totgols + dados['gols']
    gols.append(dados['gols'])
print('-='*30)
print(f'O Jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for i, v in enumerate(gols):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {totgols} gols!')
