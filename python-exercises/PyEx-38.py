#Crie a função SorteioMoeda que retorne "Cara" ou "Coroa". 

import random

def sorteio_moeda():
  lados = ["Cara", "Coroa"]
  return random.choice(lados)

print(sorteio_moeda())