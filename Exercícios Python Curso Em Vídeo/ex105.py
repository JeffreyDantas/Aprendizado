#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#–A média da turma
#– A situação (opcional)
def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos
    :param n: Dados das notas a serem calculadas
    :param sit: Situação da média (Boa, Razoável ou Ruim)
    :return: retorna os valores pedidos em dicionário!
    '''
    r = {}
    r ['Total'] = len(n)
    r ['Maior'] = max(n)
    r ['Menor'] = min(n)
    r ['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >=5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#help(notas)