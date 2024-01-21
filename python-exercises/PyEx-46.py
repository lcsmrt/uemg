#Crie a função NomedoMes que receba um parâmetro e responda com o nome do mês correspondente. 

def nome_do_mes(num):
  if num == 1:
    return "Janeiro"
  elif num == 2:
    return "Fevereiro"
  elif num == 3:
    return "Março"
  elif num == 4:
    return "Abril"
  elif num == 5:
    return "Maio"
  elif num == 6:
    return "Junho"
  elif num == 7:
    return "Julho"
  elif num == 8:
    return "Agosto"
  elif num == 9:
    return "Setembro"
  elif num == 10:
    return "Outubro"
  elif num == 11:
    return "Novembro"
  elif num == 12:
    return "Dezembro"
  else:
    return "Número não corresponde a nenhum mês."

print(nome_do_mes(10))
print(nome_do_mes(0))