#Exercício 02

ds=int(input("quantidade de dias: "))
hr=int(input("quantidade de horas: "))
min=int(input("quantidade de minutos: "))
seg=int(input("quantidade de segundos: "))
total=seg+(min*60)+(hr*60*60)+(ds*24*60*60)
print('o total em segundos: ', total)