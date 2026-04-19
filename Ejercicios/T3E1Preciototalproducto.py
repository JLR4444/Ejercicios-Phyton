# Pedir datos a la usuaria:
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio: "))
cantidad = int(input("Introduce la cantidad: "))
descuento = float(input("Introduce el descuento (%): "))
iva = float(input("Introduce el IVA (%): "))

#Definimos una funcion sin parametros
def calcular_precio_total(precio, cantidad, descuento, iva):
    total = precio * cantidad
    total_descuento = total - total * descuento / 100
    total_final = total_descuento + total_descuento * iva / 100
    return total_final

#Llamamos a la funcion
precio_final = calcular_precio_total (precio, cantidad, descuento, iva)

#Reultado finanl
print("producto", nombre)
print("precio_final", precio_final)
