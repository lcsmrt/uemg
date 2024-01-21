#Faça um programa que peça uma nota entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nt = int(input("Digite um valor entre 0 e 10: "))

while nt < 0 or nt > 10:
  print("\nValor inválido.")
  nt = int(input("Digite um valor válido: "))
else:
  print("\nFim.")