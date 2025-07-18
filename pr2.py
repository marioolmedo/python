diccUsuarios = {"Admin":"12345", "Admin2":"23456"}
user = input("Ingrese su usuario: ")
intentos = 0
if user in diccUsuarios:
    password = input("Ingrese su contraseña: ")
    #Usuario encontrado
    intentos = intentos + 1
    while intentos <= 2:
        if password == diccUsuarios[user]:
            print("Acceso Correcto")
            intentos = intentos + 3
        else:
            print("Acceso Denegado")
            intentos = intentos + 1
            password = input(f"Intentos {intentos} de 3. Reescriba la contraseña: ")
else:
    print("Usuario no encontrado")