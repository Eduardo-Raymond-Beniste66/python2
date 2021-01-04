#Incremento no fatiamento
#Verifique se uma paávra é palídrome
palavra = input('palavra:')
palidrome = palavra == palavra[::-1]
print(f'{palavra} é palídrome?')
print(palidrome)

