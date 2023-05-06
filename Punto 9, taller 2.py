
lista =(input("Ingrese una lista de numeros separados por comas: ")).split(",") # Pedimos la lista, haciendo uso de la funcion .splis para separalos caracteres

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


# FUNCION MEDIANA
def convertir (lista:list) -> list:
    ret = []
    for i in lista: # Recorremos la lista
        num = int(i) # Transformamos estos valores en enteros 
        ret.append (num) # Pegamos el nuevo numero con la funcion .append
    return ret

lista = convertir(lista) # Parametros remplazando para quedar en numeros
lista.sort() # Ordenamos la lista
tam = len(lista) # Variable para guardar tmañao de la lista
if (tam%2 > 0 ):
    mediana = lista [tam//2] # Operacion para saber que valor es el de la mitad
else: # si la lista es impar
    num1 = lista [tam//2]
    num2 = lista [tam//2] - 1 # la mediana de los dos numeros
    mediana = (num1 + num2 ) / 2
    mediana = lista[0] # Primer elemento de la lista asumiendo que es el de la lista
print("La mediana de la lista de numeros es", mediana)

# PROMEDIO MULTIPLICATIVO
from math import sqrt # Importamos funcion raiz cuadrada 
lista
resultado = sqrt(tam)
print("El promedio multiplicativo es", resultado)

tamaño = len(lista) # Tamaño


# ORDENAR DE MAYOR A MENOR
lista.sort # Hacemos usos de la funcion sort 
print("Lista en orden ascendente ",lista) # Imprimimos el resultado

# ORDENAR DE MENOR A MAYOR
lista.sort(reverse = True) 
print("Lista en orden descendente ",lista)

# POTENCIA MAYOR NUMERO ELEVADO AL MENOR NUMERO
potencia = max(lista)** min(lista) # Usamos funcion maximo y menor elemento de la lista junto con ** para elevar
print("La potencia de mayor numero elevado al menor numero es", potencia) # Imprimimos resultados

# RAIZ CUBICA DEL MENOR NUMERO

raiz = min(lista)**(1/3) # Operacion raiz cubica
print("La raiz cubica de", min(lista), "es ", raiz) # Imprimimos el resultado






