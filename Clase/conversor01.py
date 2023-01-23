menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opción = int(input(menu))

if opción == 1:
     pesos = float(input("Cuántos pesos colombianos tienes?: "))
     valor_dolar = 3875 
     dolares = pesos / valor_dolar
     dolares = round(dolares, 2)
     dolares = str(dolares)
     print("Tienes $" + dolares + " dolares")
     

elif opción == 2:
    pesos = float(input("Cuántos pesos argentinos tienes?: "))
    valor_dolar = 184.39 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
    
elif opción == 3:
    pesos = float(input("Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 18.87
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Elija una opción correcta, por favor")