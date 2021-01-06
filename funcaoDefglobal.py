#Exercicio de funçao def  fatec() global
jose = 'entoru 6h'
def fatec():
    global jose
    jose = 'entrou 8'
    print(jose)
    print(jose)
    fatec()
    print(jose)
