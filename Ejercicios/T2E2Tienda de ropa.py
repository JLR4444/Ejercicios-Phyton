#Definir los precios
camiseta = 10
sudadera = 20.5
gorra = 5.5

#Pedir cantidades de cada artículo
cantidad_camisetas = int(input("¿Cuántas camisetas quieres?"))
cantidad_sudaderas = int(input("¿Cuántas sudaderas quieres?"))
cantidad_gorras = int(input("¿Cuántas gorras quieres?"))

#Total de la compra
precio_total_camisetas = cantidad_camisetas * camiseta
precio_total_sudaderas = cantidad_sudaderas * sudadera
precio_total_gorras = cantidad_gorras * gorra


precio_total_compra = precio_total_camisetas + precio_total_sudaderas + precio_total_gorras

#Añade el 21% de IVA al total.
precio_total_con_iva = precio_total_compra + (precio_total_compra * 0.21)

#Imprimimos los resultados
print("precio total compra con iva: ", precio_total_con_iva)