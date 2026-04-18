#Frase
frase = input ("Introduce una frase: ")

#obtenemos el numero de letras de la frase
longitud = len(frase)

#poner la frase en mayusculas
mayusculas = frase.upper()

#poner la frase en minusculas
minusculas = frase.lower()


#imprimimos la palabra
print(frase)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud ", longitud)
#imprimir cadena en mayusculas
print(mayusculas)
#imprimir la cadena en minusculas
print(minusculas)