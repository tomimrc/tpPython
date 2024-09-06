dia = int(input("Ingese un dia de la semana"))
while dia not in range(8):
    dia = int(input("Ingrese un dia de la semana"))
if dia == 6 or dia == 7:
    print("Dia no laborable")
else:
    print("Dia laboral")