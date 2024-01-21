#Faça uma função que receba três parâmetros: valor, percentual e opção. Se opção for 1 o percentual será descontado do valor. Se for 2 será um acréscimo. Retorne o valor corrigido. 

def perc(v, p, o):
  if o == 1:
    return v - ((p / 100) * v)
  elif o == 2:
    return v + ((p / 100) * v)
  else:
    return "Opção inválida."

print(perc(100, 10, 1))
print(perc(100, 10, 2))