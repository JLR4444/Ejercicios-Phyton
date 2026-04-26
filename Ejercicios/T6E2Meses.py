meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Pide a la usuaria un número del 1 al 12.
numero = int(input("Introduce un número del 1 al 12: "))

if numero >= 1 and numero <= 12:
    mes = meses[numero - 1]
    print(mes)

    if mes == "Enero":
        print("EL MEJOR MES")
else:
    print("Número inválido. Debe estar entre 1 y 12.")