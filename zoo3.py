import screen

def calcularPrecioEntrada(e):
    if e > 0 and e < 3:
        precio = 0    
    elif e > 2 and e < 13:
        precio = 14
    elif e > 12 and e < 65:
        precio = 23
    else:
        precio = 18
        
    return precio

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n >= 0:
            #entonces el valor es válido
            return True
        return False
    except:
        return False

def pedirEdad():
    screen.locate(1,1)
    edad = input(" ¿Que edad tienes? ")
    while validaEdad(edad) == False:
        print("Edad Invalida")
        screen.locate(1,1)
        edad = input(" ¿Que edad tienes? ")
        
    return int(edad)
    
screen.clear()    
edad = pedirEdad()
precioTotal = 0


while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print("Precio Entrada: {}".format(precioE))
    precioTotal += precioE
    
    edad = pedirEdad()
    
print("Total: {}".format(precioTotal))