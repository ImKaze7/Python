def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Cu谩ntos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 馃挵
1
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opci贸n: """

opci贸n = int(input(menu))

if opci贸n == 1:
    conversor("colombianos", 4.58)

elif opci贸n == 2:
    conversor("argentinos", 184.40)
    
elif opci贸n == 3:
    conversor("mexicanos", 18.81)
    
else:
    print("Elija una opci贸n correcta, por favor")