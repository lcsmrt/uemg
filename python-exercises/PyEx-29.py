#Crie um programa que grave em um arquivo de nome random.txt uma lista de 20 números aleatórios entre 100 e 999.

import random

lista = random.sample(range(100, 1000), 20)

file = open("random.txt", "w")
file.write(str(lista))
file.close()
print("Lista gravada com sucesso.")