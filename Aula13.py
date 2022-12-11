nome = 'Anthony'
altura = 1.90
peso = 115
imc = peso / (altura**2) # IMC = PESO / (ALTURA x Altura)

#Ellipsis = ...

linha1 = 'nome tem altura de altura'


# Formatação, f antes da string, variavel dentro de {}, casas decimais :2f = 10.00, :,3f = 10.000, ,.2f = 10,00
print(f'Anthony tem 1.90 de altura, pesa 115 quilos e seu IMC é: {imc:.2f}')
 