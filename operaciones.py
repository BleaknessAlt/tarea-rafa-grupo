def comprobarInt(num1, num2):
    return True if type(num1) == int and type(num2) == int else False


def comprobarFloat(num1, num2):
    return True if type(num1) == float and type(num2) == float else False


def comprobarTipos(num1, num2):
    return True if comprobarInt(num1, num2) and comprobarFloat(num1, num2) else False


def sumar(num1, num2):
    if comprobarTipos(num1, num2):
        return num1 + num2


def restar(num1, num2):
    if comprobarTipos(num1, num2):
        return num1 - num2


def multiplicar(num1, num2):
    numero = 0
    if comprobarTipos(num1, num2):
        for i in range(num2):
            numero += num1
            
    return numero

def dividir(num1, num2):
    esInt1 = isistance(num1, int)
    esInt2 = isistance(num2, int)

