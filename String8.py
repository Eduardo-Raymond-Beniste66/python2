#Exerício
#Faça um programa que solicite a data de
#nascimento (dd/mm/aaaa) e imprima com o
#nome por extenso
mes = '''janeirofevereiro março
abril maio junho julho agosto
setembro outubro novembro
dezembro'''.split()
d,m,a=input('dd/mm/aaaa:').split('/')
print(f'{d} de{mes[int(m)-1]}de{a}')
