#Exercício 14

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
if (n1 > n2 > n3):
  print("O maior é", n1, "e o menor é", n3)
elif (n1 > n3 > n2):
  print("O maior é", n1, "e o menor é", n2)
elif (n2 > n1 > n3):
  print("O maior é", n2, "e o menor é", n3)
elif (n2 > n3 > n1):
  print("O maior é", n2, "e o menor é", n1)
elif (n3 > n1 > n2):
  print("O maior é", n3, "e o menor é", n2)
else:
  print("O maior é", n3, "e o menor é", n1)