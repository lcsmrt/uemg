#Altere a função agora para também mostrar o percentual.

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
  return str("Total de Caras: " + str(cara.count(0)) + " (" + str((cara.count(0) * 100) / qtd)+"%)\nTotal de Coroas: " + str(coroa.count(1)) + " (" + str((coroa.count(1) * 100) / qtd)+"%)")

print(sorteio_moeda(100))