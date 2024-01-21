#Exercício 17

areap = float(input("Área a ser pintada (m²):"))
litr = areap / 3
lat = -(-litr // 18)
prec = lat * 80
print("Quantidade de latas:", lat, "\nPreço: R$", prec)
