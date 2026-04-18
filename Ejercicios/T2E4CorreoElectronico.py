#Introducir correo electronico
correo = input ("Introduce un correo electronico: ")

#obtenemos el numero de letras de la frase
longitud = len(correo)

#poner la frase en mayusculas
mayusculas = correo.upper()

#poner la frase en minusculas
minusculas = correo.lower()


#imprimimos la palabra
print(correo)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud ", longitud)
#imprimir cadena en mayusculas
print(mayusculas)
#imprimir la cadena en minusculas
print(minusculas)