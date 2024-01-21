import requests

class Dolar():
  
  def __init__(self):
    self.valor = 0

  def consulta(self):
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    self.valor = cotacao['USD']['bid']