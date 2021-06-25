from functools import reduce
import pdb

def mayor(lst):
#    pdb.set_trace()
    mayor = 1
    for i in lst:
        if i > mayor:
            mayor = i
    return mayor

lista1 = [i for i in range(1,9)]
lista2 = [i for i in range(100, 500, 50)]


print(mayor(lista1))
#print(mayor(lista2))

lista3 = list(range(1, 200))


def primos(n):
    primo = True
    for i in range(2, n):
        if(n % i == 0):
            primo = False
    return primo

primos = list(filter(primos, lista3))

print(primos)
