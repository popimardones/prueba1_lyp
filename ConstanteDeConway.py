def lookAndSay(numero):
    resultado = ""

    repeat = numero[0]
    numero = numero[1:] + " "
    veces = 1

    for actual in numero:
        if actual != repeat:
            resultado += str(veces) + repeat
            veces = 1
            repeat = actual
        else:
            veces += 1

    return resultado


num = "1"

for i in range(10):
    print(num)
    num = lookAndSay(num)