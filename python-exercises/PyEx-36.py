#Crie a função Semvogal que receba uma palavra e retorne essa palavra escrita sem as vogais (caso existam). 

def semvogal(pal):
  if (pal.count('a') > 0) or (pal.count('e') > 0) or (pal.count('i') > 0) or (pal.count('o') > 0) or (pal.count('u') > 0):
    pal = pal.replace('a', '')
    pal = pal.replace('e', '')
    pal = pal.replace('i', '')
    pal = pal.replace('o', '')
    pal = pal.replace('u', '')
  return pal

print(semvogal("Tasta, teste, tisti, tosto, tustu"))