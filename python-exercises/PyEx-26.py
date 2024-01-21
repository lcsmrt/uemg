#Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random

lista = []; par = []; impar = []

while len(lista) < 20:
  lista.append(random.randint(1, 100))
else:
  lista.sort()
  for n in lista:
    if(n % 2 == 0):
      par.append(n)
    else:
      impar.append(n)

print("Lista:\n", lista, "\n\nLista Par:\n", par, "\n\nLista Impar:\n", impar)