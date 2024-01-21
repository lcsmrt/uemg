#Altere a função SorteioMoeda para receber um parâmetro de quantidade de sorteios a serem feitos e retorne uma string contendo o total de pares e ímpares no resultado.

import random

def sorteio_moeda(qtd):
  lados = ["Cara", "Coroa"]
  cara = []
  coroa = []
  for x in range(qtd):
    if random.choice(lados) == "Cara":
      cara.append(0)
    else:
      coroa.append(1)
  return str("Total de Caras: " + str(cara.count(0)) + "\nTotal de Coroas: " + str(coroa.count(1)))

print(sorteio_moeda(10))