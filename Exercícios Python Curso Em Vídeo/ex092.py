#Crie um programa que leia nome, ano de nascimento e carteira de trabalho, e cadastre-os com idade em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - dados['idade']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (35 - (date.today().year - dados['contrato']))
print('-='*30)
print(dados['nome'])
print(f'com {dados["idade"]} anos')
print(f'Carteira de Trabalho número: {dados["ctps"]}')
if dados['ctps'] != 0:
    print(f'Contratado no ano de {dados["contrato"]}')
    print(f'Com salário de R$ {dados["salario"]}')
    print(f'Irá se aposentar com {dados["aposentadoria"]} anos de idade!')
print('-='*30)
