#1 sorteio 10 inteiros entre 1 e 100 para uma lista
#e descubra o maior e menor valor sem usar
#as funções max e min

print('----programa que sorteia 10 inteiros entre 1 e 100----')
from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
for x in vetor[1:]:
  if x > maior: maior = x
  if x < menor: menor = x
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')



