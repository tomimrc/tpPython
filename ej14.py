import random
nro = random.randint(0,100)
print(nro)
encontrado = False
intentos = 0

while encontrado == False:
    opcion = int(input("Indique que numero se generó aleatoriamente"))
    intentos = intentos +1
    if opcion == nro:  
        print("Correcto, el nro es ", nro, "cantidad de intentos: ",intentos)
        encontrado == True
        break
    elif opcion <= nro:
        print("el nro ingresado es muy bajo")
        
    elif opcion >= nro:
        print("el nro ingresado es muy alto")
        

