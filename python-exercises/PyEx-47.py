#Crie uma função chamada AnteeSuce que receba um número e retorne com o seu antecessor e seu sucessor. 

def ante_e_suce(num):
  return str("Número: " + str(num) + "\nAntecessor: " + str(num - 1) + "\nSucessor: " + str(num + 1))

print(ante_e_suce(10))