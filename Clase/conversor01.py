def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("Cuántos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰
1
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opción = int(input(menu))

if opción == 1:
    conversor("colombianos", 4.58)

elif opción == 2:
    conversor("argentinos", 184.40)
    
elif opción == 3:
    conversor("mexicanos", 18.81)
    
else:
    print("Elija una opción correcta, por favor")