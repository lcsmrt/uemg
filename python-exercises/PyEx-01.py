'''

Usando o conceito de POO, desenvolver dentro do python uma classe chamada conta que deverá conter os atributos saldo, tipo_da_conta (P ou C) e os seguintes métodos:
Creditar
Debitar
exibirSaldo
exibirTipoDaConta
ModarParaPupança
MudarParaContaCorrente
Render - Recebe um percentual de juros e aplica ao saldo
(Os dois atributos deverão ser privados)

Ao ser instanciada deverá ter o seu saldo zerado. Toda nova conta criada automaticamente será corrente.

'''

class Conta:
  def __init__(self):
    self.__saldo = 0
    self.__tipo_da_conta = "C"

  def Creditar(self, valor):
    self.__saldo += valor

  def Debitar(self, valor):
    self.__saldo -= valor

  def exibirSaldo(self):
    return self.__saldo

  def exibirTipoDaConta(self):
    return self.__tipo_da_conta

  def MudarParaPoupanca(self):
    self.__tipo_da_conta = "P"

  def MudarParaContaCorrente(self):
    self.__tipo_da_conta = "C"

  def Render(self, juros):
    self.__saldo += self.__saldo*(juros/100)

conta = Conta()

conta.Creditar(600)
print(conta.exibirSaldo())
conta.Debitar(60)
print(conta.exibirSaldo())
print(conta.exibirTipoDaConta())
conta.MudarParaPoupanca()
print(conta.exibirTipoDaConta())
conta.Render(2)
print(conta.exibirSaldo())