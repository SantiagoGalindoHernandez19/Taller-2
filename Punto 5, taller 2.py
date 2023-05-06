
def mcm(x, y): #definimos el minimo comun multiplo de x, y
    z = max(x, y) #definimos z

    while True:
        if (z % y == 0): #establecemos la formula del mcm
            return z

        z += 1

print(mcm(17, 15)) #manejamos los dos numeros y obtenemos la respuesta

