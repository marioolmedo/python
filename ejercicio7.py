#Programa que imprima numeros primos

n = 0
n = int(input("Ingrese desde qué numero empezar: "))
while True:
    esPrimo = True
    for x in range(2, int(n/2)):
        if n % x == 0:
            esPrimo = False
            break
    if esPrimo :
        print(f"Es primo: {n}")
    n = n+1


    