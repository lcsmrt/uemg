#Crie uma função que receba a nota de 3 provas e retorne a média ponderada desses valores. A primeira prova tem peso 3, a segunda 1 e a terceira tem peso 4. 

def medpon(p1, p2, p3):
  return ((p1 * 3) + p2 + (p3 * 4)) / (3 + 1 + 4)

print(medpon(20,25,30))