#Exercício 16

salh = float(input("Informe o salário-hora:"))
numh = int(input("Informe o número de horas:"))
salb = salh * numh
ir = salb * 0.11
inss = salb * 0.08
sin = salb * 0.05
sall = salb - (ir + inss + sin)
print("a)Salário Bruto: R$", salb, "\nb)IR (11%): R$", ir, "\nc)INSS (8%): R$", inss, "\nd)Sindicato (5%): R$", sin, "\ne)Salário Líquido: R$", sall)