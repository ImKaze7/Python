#Factura
"""
importe
100

IGV
(+)18%  0.18

total
118

"""
#Ingreso De Datos
importe = float(input("Ingrese el importe: "))

#Cálculo
IGV = importe * 0.18
total = IGV + importe

#Saliente
print("El total es: ",total)
