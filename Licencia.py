#Desarrollado por Mario
edad = int(input("Ingrese su edad: "))

print(f"Usted tiene {edad} años de edad")

if 18 <= edad <= 60:
    print("Acceda a la Licencia de Adulto")
elif 15 < edad < 18:
    print("Acceda a la Licencia de Menor")
else:
    print("Usted no puede tener licencia")
    if edad < 18:
        x = 16 edad
        print(f"Vuelva dentro de {x} años") 