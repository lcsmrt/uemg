#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usern = str(input("Usuário: "))
passw = str(input("Senha: "))

while usern == passw:
  print("\nERRO. A senha não pode ser igual ao nome de usuário. \nDigite novamente.")
  usern = str(input("\nUsuário: "))
  passw = str(input("Senha: "))
else:
  print("\nCadastro realizado.")