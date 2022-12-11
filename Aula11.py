# PRECEDENCIA DOS OPERADORES, COMPUTADO PRIMEIRO

# 1. (n+n) , executa primeiro em parenteses, no caso se for interno também
# ex: (1+2 *(1+5)), executa o interno primeiro.
# 2. **
# 3. * / // %
# 4. + - 

conta1 = 1 + 1 ** 5 + 5 #7
print(conta1)
conta2 = 1+1 - (2*10-5) % 2 #1
print(conta2)