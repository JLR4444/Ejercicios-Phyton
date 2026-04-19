# Pedir datos a la usuaria:
euros = float(input("Introduce una cantidad de euros: "))

#Definimos una funcion sin parametros
def convertirMoneda(euros):
    dolares = euros * 1.1
    libras = euros * 0.87
    return dolares, libras

#Llamamos a la funcion
dolares, libras = convertirMoneda(euros)

#Reultado finanl
print("euros", euros)
print("dolares", dolares)
print("libras", libras)