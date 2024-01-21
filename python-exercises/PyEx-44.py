#Crie uma função que receba como parâmetro um número e responda se ele é divisível por 3 e por 5 ao mesmo tempo. 

def ediv(num):
  if (num % 3 == 0) and (num % 5 == 0):
    return "O número é divisível por 3 e por 5 ao mesmo tempo."
  else:
    return "O número não é divisível por 3 e por 5 ao mesmo tempo."
print(ediv(15))
print(ediv(2))