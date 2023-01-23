# 4 notas Examenes
#15+11+18+13



primera_nota = float(input("La primera nota es: "))
segunda_nota = float(input("La segunda nota es: "))
tercera_nota = float(input("La tercera nota es: "))
cuarta_nota = float(input("La cuarta nota es: "))

#Cálculo

total_de_notas = (primera_nota + segunda_nota + tercera_nota + cuarta_nota) / 4

#Condicion

if total_de_notas > 11:
    print(total_de_notas, "Estás aprobado")
else:
    print(total_de_notas, "Estás desaprobado")  