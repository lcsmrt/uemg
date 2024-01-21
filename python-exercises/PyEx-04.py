#Exercício 04

prmer=float(input("preço da mercadoria: "))
desc=float(input("percentual de desconto: "))
valdesc=(prmer*desc/100)
newpr=(prmer-valdesc)
print('valor do desconto: ', valdesc)
print('novo preço: ', newpr)