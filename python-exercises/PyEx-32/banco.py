import sqlite3
from dolar import Dolar

Dolar = Dolar()
Dolar.consulta()

class Banco():
  def __init__(self):
    self.conexao = sqlite3.connect("JLComercio.db")
    self.cursor = self.conexao.cursor()

  def _close(self):
    self.conexao.close()

  def create(self):
    try:
      self.cursor.execute("DROP TABLE if exists produtos")
      self.cursor.execute("CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, quantidade INT, valor DECIMAL)")   
            
    except sqlite3.OperationalError:
      print ("\nErro ao criar a tabela.")

    self.conexao.commit()

  def list(self):
    self.cursor.execute("SELECT * FROM produtos")

    for x in self.cursor.fetchall():
      print(x)

  def insert(self):
    nome = input("\nNome: ")
    quantidade = input("Quantidade: ")
    custo = input("\nCusto: " )
    valor = float(input("Valor: "))
    self.cursor.execute("INSERT INTO produtos (nome, quantidade, valor) VALUES (?, ?, ?)", (nome, quantidade, valor))
    self.conexao.commit()

  def delete(self):
    id = input("\nID: ")
    self.cursor.execute("DELETE FROM produtos WHERE id = ?", id)
    self.conexao.commit()

  def alter(self):
    id = input("\nID: ")
    self.nome = input("Nome: ")
    self.valor = float(input("Valor: "))
    self.cursor.execute("UPDATE produtos SET nome = ?, valor = ? WHERE id = ?", (self.nome, self.valor, id))
    self.conexao.commit()
  
  def inpt(self):
    id = input("\nID: ")
    quantidade = int(input("Quantidade: "))
    self.cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?", (quantidade, id))
    self.conexao.commit()

  def outpt(self):
    id = input("\nID: ")
    quantidade = int(input("Quantidade: "))
    self.cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (quantidade, id))
    self.conexao.commit()

  def list_dollar(self):
    print("\nValor atual do dolar: " + str(Dolar.valor) + "\n")
    self.cursor.execute("SELECT nome, valor, (valor * ?) AS valor_em_dolar FROM produtos", (Dolar.valor,))
    for x in self.cursor.fetchall():
      print(x)
    self.cursor.execute("SELECT SUM(valor *?) FROM produtos", (Dolar.valor,))
    print("\nTotal em dolares dos produtos do estoque:" + str(self.cursor.fetchall()))

  def att(self):
    pcnt = int(input("\nInsira a porcentagem de aumento: "))
    self.cursor.execute("UPDATE produtos SET valor = valor * (?/100.0) ", (pcnt,))
    self.conexao.commit()

  def quit(self):
    self._close()