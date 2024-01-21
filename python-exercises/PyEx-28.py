#Crie um programa que exiba um menu com 3 opções: 1 – Gravar Data, 2 – Gravar nome e 3 – Sair. Se for escolhida a opção 1 deverá ser criado um arquivo com o nome de data.txt e dentro dele deverá constar a data de hoje. Se for escolhida a opção 2 deverá ser perguntado o nome e gravado dentro do arquivo nome.txt o nome digitado. Se for escolhido a opção 3 deverá sair.

from datetime import datetime

n = int(input("1 - Gravar Data\n2 - Gravar Nome\n3 - Sair\n\nOpção: "))
agora = datetime.now()

while n != 3:
  if(n == 1):
    file = open("data.txt", "w")
    file.write(agora.strftime("%d/%m/%Y"))
    file.close()
    print("\nData gravada com sucesso.")
    n = int(input("\nOpção: "))
  elif(n == 2):
    file = open("nome.txt", "w")
    file.write(str(input("\nNome: ")))
    file.close()
    print("\nNome gravado com sucesso.")
    n = int(input("\nOpção: "))
  else:
    print("\nOperação inválida.")
    n = int(input("\nDigite uma opção válida: "))

print("\nMenu encerrado.")