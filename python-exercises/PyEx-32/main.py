from banco import Banco

Banco = Banco()
opc = None

Banco.create()

def menu():
  print("1 - Listar Produtos")
  print("2 - Inserir Produto")
  print("3 - Excluir Produto")
  print("4 - Alterar Produto")
  print("5 - Entrada no Estoque")
  print("6 - Saída no Estoque")
  print("7 - Listar Produtos com Valor em Dólar")
  print("8 - Atualizar Valor")
  print("9 - Sair")

  opc = int(input("Insira a opção escolhida: "))

  if(opc == 1):
    Banco.list()
  elif (opc == 2):
    Banco.insert()
  elif (opc == 3):
    Banco.delete()
  elif (opc == 4):
    Banco.alter()
  elif (opc == 5):
    Banco.inpt()
  elif (opc == 6):
    Banco.outpt()
  elif (opc == 7):
    Banco.list_dollar()
  elif (opc == 8):
    Banco.att()
  elif (opc == 9):
    Banco.quit()

menu()