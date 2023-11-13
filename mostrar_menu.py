from operaciones import sumar, restar, multiplicar, comprobarTipos


def mostrar_menu():
    print(
        " _____       ___   _       _____   _   _   _           ___   _____   _____   _____   "
    )
    print(
        "/  ___|     /   | | |     /  ___| | | | | | |         /   | |_   _| /  _  \ |  _  \  "
    )
    print(
        "| |        / /| | | |     | |     | | | | | |        / /| |   | |   | | | | | |_| |  "
    )
    print(
        "| |       / / | | | |     | |     | | | | | |       / / | |   | |   | | | | |  _  /  "
    )
    print(
        "| |___   / /  | | | |___  | |___  | |_| | | |___   / /  | |   | |   | |_| | | | \ \  "
    )
    print(
        "\_____| /_/   |_| |_____| \_____| \_____/ |_____| /_/   |_|   |_|   \_____/ |_|  \_\ "
    )

    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    eleccion = input("Que deseas hacer: ")


def menuOpciones(elecciones):
    if elecciones == 1:
        valores = pedirValores()
        if comprobarTipos(valores[0], valores[1]):
            sumar(valores[0], valores[1])
        else:
            print("Los valores introducidos no son los correctos.")
    if elecciones == 2:
        valores = pedirValores()
        if comprobarTipos(valores[0], valores[1]):
            restar(valores[0], valores[1])
        else:
            print("Los valores introducidos no son los correctos.")
    if elecciones == 3:
        valores = pedirValores()
        if comprobarTipos(valores[0], valores[1]):
            multiplicar(valores[0], valores[1])
        else:
            print("Los valores introducidos no son los correctos.")

    if elecciones == 4:
        valores = pedirValores()
        if comprobarTipos(valores[0], valores[1]):
            """"""
        else:
            print("Los valores introducidos no son los correctos.")


def pedirValores():
    print("Debe de introducir dos valores")
    valor1 = input("Introduzca el primer valor")
    valor2 = input("Introduzca el segundo valor")
    return [valor1, valor2]
