#Exercício 15

peso = float(input("Insira o peso(kg): "))
if peso > 50 :
  pesoex = peso - 50
  multa = pesoex * 4
  print("O peso excedeu.\nExcedente:", pesoex, "\nMulta:", multa)
else :
  pesoex = 0 
  multa = 0
  print("Peso dentro do regulamento.")