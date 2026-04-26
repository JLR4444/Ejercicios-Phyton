#Pide a la usuaria cuántas notas desea introducir. 
cantidad = int(input("¿Cuántas notas quieres introducir?: "))

suma = 0

for i in range(cantidad):
    nota = float(input("Introduce una nota: "))
    suma = suma + nota

media = suma / cantidad

print("La media es:", media)