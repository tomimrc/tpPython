contraseña = "asdqwe"
intentos = 0

while intentos < 3:
    ingresado = input("Ingrese su contraseña")
    if ingresado == contraseña:
        print("Acceso Correcto")
        break
    else:
        print(ingresado)
        intentos = intentos + 1