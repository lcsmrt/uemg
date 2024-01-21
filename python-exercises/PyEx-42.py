#Crie a função CriaTitulo que receba uma palavra e retorne ela dentro de um quadrado desenhado com os caracteres +,- e |. 

def cria_titulo(pal):
  l1 = ["+", "-", "+", "-"]
  l2 = ["+", "-", "+", "-"]
  c = 3
  for x in range(len(pal)):
    if l1[c] == "+":
      l1.append("-")
    elif l1[c] == "-":
      l1.append("+")
    if l2[c] == "+":
      l2.append("-")
    elif l2[c] == "-":
      l2.append("+")
    c += 1
  l1 = ''.join(l1)
  l2 = ''.join(l2)

  print(l1)
  print("| " + pal + " |") 
  print(l2)

cria_titulo("Teste")
cria_titulo("Teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeste")