num = int(input("Ingrese un nro"))
contador = 0
for iteracion in range(num +1):
    iteracion = iteracion +1 
    if num <= 1:
        print("el num no es primo")
        break
    elif contador > 2:
        print("El numero no es primo")
        break
    elif num % iteracion == 0:
        contador = contador +1
        if iteracion == num and contador <= 2:
            print("el nro es primo")
    
    


