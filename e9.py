import os

while True:
    os.system("cls")
    print("1. Calculadora")
    print("2. Chrome")
    print("0. Salir")
    opción = input("Opción: ")
    if opción == "1":
        os.system("Calc")
    elif opción == "2":
        os.system("start Chrome")
    elif opción == "0":
        break
    else:
        print("????")
