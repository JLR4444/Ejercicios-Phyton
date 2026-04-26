#Pedir a la usuaria 5 veces que introduzca un color
for i in range(5):
    color = input ("Introduce un color: ")

if color == "azul":
    print("¡Has ganado!")
else:
    print("¡Prueba otro color!")



# Hay algo que no me cuadra en el color porque si lo introduce 5 veces y luego en una de las veces es azul, igualmente sale que pruebe con otro color... 