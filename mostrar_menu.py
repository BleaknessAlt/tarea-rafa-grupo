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
        """"""
    elif elecciones == 2:
        """"""

    elif elecciones == 3:
        """"""

def pedirValores():
    print("Debe de introducir dos valores")
    valor1 = input("Introduzca el primer valor")
    valor2 = input("Introduzca el segundo valor")
    
    return [valor1,valor2]

def comprobarInt(num1, num2):
    return True if type(num1) == int and type(num2) == int else False
    

def comprobarFloat(num1, num2):
    return True if type(num1) == float and type(num2) == float else False


def comprobarValores(num1, num2):
    return comprobarInt(num1) and comprobarFloat(num1, num2)
