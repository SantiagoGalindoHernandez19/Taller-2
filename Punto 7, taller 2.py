
lista =(input("Ingrese una lista de numeros separados por comas:   ")).split(",") # Pedimos la lista, haciendo uso de la funcion .splis para separalos caracteres

# FUNCION PROMEDIO 
suma = 0 # Suma de todos los numeros
CuantosPositivos = 0 # Cuales numeros son positivos y no tomar en cuenta los negativos
for i in lista: # Recorrer la lista
    num = int(i) # Defnimos el termino i como numero para operarlo
    if (num > 0):
        suma += num  # Sumamos solo si es un numero positivo
        CuantosPositivos += 1
promedio = suma/CuantosPositivos # Realizamos la correcta operacion
print("El promedio de la lista de numeros es", promedio) # Imprimimos el resultados 