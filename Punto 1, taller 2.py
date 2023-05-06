numeros = [ ] #Creacion lista
def separadig(x): # Definimos la variable con la funcion
    while x > 0:  # Usamos un ciclo 
        print(x%10) #Muestre el ultimo digito 
        numeros.append(x % 10)
        x = x // 10 # Operacion para minimizar el numero hasta 0 
    print(numeros[:])   

n = int(input("Ingrese un numero entero:")) # Pedimos ingresar numero 
separadig(n) 
