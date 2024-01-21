#Exercício 09

import random

lista = random.sample(range(20, 50), 10)
soma = 0

for x in lista:
  soma += x

print(soma)