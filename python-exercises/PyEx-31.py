#Crie um programa que leia o conteúdo do arquivo random.txt e exiba na tela os números pares ali existentes.

def posic(n):
  n = (6 + (n - 2) * 5)
  return n

file = open("random.txt", "r")
cnt = 1
pares = []; impares = []

while cnt < 20:
  pos = posic(cnt)
  file.seek(pos, 0)
  cnt += 1
  num = file.read(3)
  if(int(num) % 2 == 0):
    pares.append(num)
  else:
    impares.append(num)

print("Lista de pares:\n\n", pares, "\n\nLista de impares:\n\n", impares)