def divisible():
    num = int(input("Ingrese un nro"))
    resultado = (num % 2 == 0)
    if resultado:
        print("es divisible")
    else:
        print("no es divisible")

divisible()