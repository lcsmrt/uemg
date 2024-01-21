#Crie a função Reverter que receba uma palavra e retorne essa palavra escrita na ordem inversa. 

def revpal(pal):
  rev = list(pal)
  rev.reverse()
  rev = ''.join(rev)
  return rev

print(revpal("Teste"))