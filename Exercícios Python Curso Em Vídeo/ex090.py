#Faça um programa que leia nome e média de um aluno, guardando em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
#E diga se o aluno foi ou não Aprovado!
dados = {}
dados['nome'] = str(input('Nome: '))
dados['Média']= float(input(f'Média de {dados["nome"]}: '))
if dados['Média'] >= 7:
    resultado = 'APROVADO!'
elif dados['Média'] > 5 < 7:
    resultado = 'RECUPERAÇÃO'
else:
    resultado = 'REPROVADO!'
print(f'O Aluno {dados["nome"]}!')
print(f'Com média {dados["Média"]}!')
print(f'Tem a situação de "{resultado}"!')