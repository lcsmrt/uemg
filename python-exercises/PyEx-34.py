#Faça uma função que receba uma palavra e retorne uma string assim "Você escreveu a palavra XXXXX e ela possui Y letras". Ou seja, a palavra deverá retornar em maiúsculas e mostrar a quantidade de letras. 

def pal(pal):
  return "Você escreveu a palavra", pal.upper(), "e ela possui", len(pal), "letras."

print(pal("Teste"))