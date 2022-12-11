# IF AND ELSE
nome = str(input('Diga seu nome: '))
sobrenome = str(input('Diga seu sobrenome: '))
idade = int(input('Diga sua idade: '))
ano_nascimento = 2022 - idade
maior_de_idade = bool(idade >= 18)
altura_metros = float(input('Diga usa altura: '))

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de Nascimento: ', ano_nascimento)
if maior_de_idade == True:
    print('É maior de idade? Sim.')
else:
    print('É maior de idade? Não.')
print('Altura em mentros: ', altura_metros)
