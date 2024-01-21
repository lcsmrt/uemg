#Exercício 18

l1 = float(input("Lado 01: "))
l2 = float(input("Lado 02: "))
l3 = float(input("Lado 03: "))
if abs(l1 - l2) < l3 < l1 + l2 or abs(l1 - l3) < l2 < l1 + l3 or abs(l2 - l3) < l1 < l2 + l3 :
  if l1 != l2 != l3 :
    print("Triângulo Escaleno.")
  elif l1 == l2 == l3 :
    print("Triângulo Equilátero.")
  else :
    print("Triângulo Isósceles.")
else:
  print("Não é possível formar um triângulo cujos lados tenham as medidas informadas.")