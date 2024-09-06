nro = int(input("ingrese un nro"))
nroStr = str(nro)
ultimoDigito = int(nroStr[-1])
length = len(nroStr)
suma = 0
divisible3 = False
divisible9 = False


if nro % 2 == 0 :
    print("Es divisible por 2")

for i in range(0, length):
    suma = suma + int(nroStr[i])
    if suma % 3 == 0:
        print("Es divisible por 3")
        divisible3 = True

if ultimoDigito == 0 or ultimoDigito == 5 :
    print("Es divisible por 5")

if nro % 2 == 0 and divisible3 :
    print("Es divisible por 6")

for i in range(0, length):
    suma = suma + int(nroStr[i])
    if suma % 9 == 0:
        print("Es divisible por 9")
        divisible3 = True


if ultimoDigito == 0:
    print("Es divisible por 10")