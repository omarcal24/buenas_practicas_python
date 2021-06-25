def sumaCuadrados(n):
    sumaCuadrados = 0
    while(n):
        sumaCuadrados += (n % 10) * (n % 10)
        n = n // 10
    return sumaCuadrados


def esNumeroFeliz(n):
    s = n
    f = n
    while(True):
       s = sumaCuadrados(s)
       f = sumaCuadrados(sumaCuadrados(f))
       if(s != f):
           continue
       else:
           break
    return(s == 1)


def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        print(i)
        resultado *= i
    return resultado


def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n % i == 0):
            primo = False
    return primo


def listar_n_primos(n):
    for i in range(2, n+1):
        if(es_primo(i)):
            print("f{i} es primo")


print(factorial(5))