#Crie uma função que receba uma palavra e retorne essa palavra com as letras misturadas de forma randômica.

import random

def mistpal(pal):
  mist = list(pal)
  random.shuffle(mist)
  mist = ''.join(mist)
  return mist

print(mistpal("Teste"))