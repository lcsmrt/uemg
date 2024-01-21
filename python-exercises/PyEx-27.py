#Crie uma função em Python usando def que receba 3 números sendo a,b e c. Retorne a soma dos 3 números. Mas caso algum número seja repetido ele não entra na soma.

def soma(a, b, c):
  lista = [a, b, c]
  for n in lista:
    if lista.count(n) > 1:
      return (a + b + c) - ((lista.count(n)-1) * n)
    else:
      return a + b + c

print(soma(1,2,3))
print(soma(1,1,3))
print(soma(1,1,1))