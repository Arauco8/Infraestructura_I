# El Cifrado César

TAM_MAX_CLAVE = 26

def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar o descifrar por fuerza bruta un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d bruta b'.split():
            return modo

        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d" o "bruta" o "b"')

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''
    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave           
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26           
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduccion += chr(num)
        else:
            traduccion += simbolo
            
    return traduccion
            
modo = obtenerModo()
mensaje = obtenerMensaje()
if modo[0] != 'b':
    clave = obtenerClave()
print('Tu texto traducido es:')
if modo[0] != 'b':
    print(obtenerMensajeTraducido(modo, mensaje, clave))
else:
    for clave in range(1, TAM_MAX_CLAVE + 1):
        print(clave, obtenerMensajeTraducido('desencriptar', mensaje, clave))

# Estos cambios piden una clave al usuario si no se encuentra en el modo de "fuerza bruta". Se efectúa entonces 
# la llamada original a obtenerMensajeTraducido() y se muestra la cadena traducida.

# Sin embargo, si el usuario está en el modo de "fuerza bruta" entonces obtenerMensajeTraducido() se ejecuta en 
# un bucle que recorre todos los valores entre 1 y TAM_MAX_CLAVE (que es 26). Recuerda que la función range() 
# devuelve una lista de enteros hasta el segundo parámetro pero sin incluirlo, por lo que agregamos + 1 a la 
# expresión. Este programa imprimirá en la pantalla cada posible traducción del mensaje (incluyendo el número 
# de clave usado para la traducción).