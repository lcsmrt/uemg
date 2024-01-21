#Exercício 21

from datetime import datetime
ano = int(input("Digite o ano: "))
agora = datetime.now()
anoat = int(agora.strftime('%Y'))
anolist = list(range(ano, anoat +1))
for ano in anolist:
  if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print(ano,"*")
  else:
    print(ano)