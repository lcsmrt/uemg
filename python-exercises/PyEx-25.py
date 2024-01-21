#Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random

lista = []
cnt = 0

while len(lista) < 10:
  lista.insert(cnt, random.randint(1, 100))
  cnt += 1
else:
  print(lista)
  lista.sort()
  print("\nMenor valor:", lista[0],"\nMaior valor:", lista[9])