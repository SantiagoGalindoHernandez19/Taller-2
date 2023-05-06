
lista = input("Ingrese una lista de numeros separados por comas: ").split(",") # Designamos el valor solicitado para la lista

if len (lista) == len(set(lista)): # Con ayuda de condicional especificamos la igualdad o diferencia de sus elementos, (set) comando utilizado para almacenar
    print("No existen elementos repetidos")
else:
    print("Hay elementos repetidos") # Imprimimos resultado contrario
    