#Crie um programa que leia o conteúdo do arquivo random.txt e exiba na tela o terceiro e o décimo número.

def posic(n):
  n = (6 + (n - 2) * 5)
  return n

file = open("random.txt", "r")
pos = posic(3)
file.seek(pos, 0)
num = file.read(3)
print(num)
pos = posic(10)
file.seek(pos, 0)
num = file.read(3)
print(num)