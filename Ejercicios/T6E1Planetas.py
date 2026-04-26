planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#Pedir al usuario un numero
numero = int(input("Introduce un número del 1 al 8: "))

if numero >= 1 and numero <= 8:
    print(planetas[numero - 1])

else:
    print("Número inválido. Debe estar entre 1 y 8.")