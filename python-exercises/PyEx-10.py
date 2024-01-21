#Ecercício 10

class Veiculo:
  def init(self):
    self.NumeroDeRodas = 4
    self.Cor = "Preto"

class Carro(Veiculo):
  def init(self):
    self.NumeroDeRodas = 4
    self.Cor = "Preto"
    self.Motorização = bool(1)

  def buzina(self):
    print("Biiiii")

uno = Carro()
uno.buzina()