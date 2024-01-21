#Crie uma função chamada SorteioDado que retorne um número inteiro entre 1 e 6 de forma randômica. 

import random

def sorteio_dado():
  lados = [1, 2, 3, 4, 5, 6]
  return random.choice(lados)

print(sorteio_dado())