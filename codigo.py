import random


ppt = int(input("Ingrese su eleccion:\n 1 = piedra \n 2 = papel \n 3 = tijeras \n numero: " ))



computadora = random.randint(1,3)
piedra  = 1
papel = 2
tijeras = 3


if(ppt == computadora):
    rta = "empate: los dos sacaron lo mismo"
elif(ppt == 1 and computadora == 2):
    rta = "la computadora saco papel. GANO LA COMPUTADORA"
elif(ppt == 2 and computadora == 1):
    rta = "la computadora saco piedra. GANASTE"
elif(ppt == 2 and computadora == 3):
    rta = "la computadora saco tijeras. GANO LA COMPUTADORA"
elif(ppt == 3 and computadora == 2):
    rta = "la computadora saco papel. GANASTE"
elif(ppt == 1 and computadora == 3):
    rta = "la computadora saco tijeras. GANASTE"
elif(ppt == 3 and computadora == 1):
    rta = "la computadora saco piedra. GANO LA COMPUTADORA"
else:
    rta = "ingrese un valor de 1 a 3"

print(str(rta))