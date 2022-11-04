# El Cifrado César

# La clave para el Cifrado César será un número entre 1 y 26. A menos que conozcas la clave (es decir, conozcas el número 
# usado para encriptar el mensaje), no podrás desencriptar el código secreto.

# El Cifrado César fue uno de los primeros sistemas de cifrado que se inventaron. Con este cifrado, para encriptar un mensaje 
# se toma cada letra del mismo (en criptografía, estas letras se llaman símbolos porque pueden ser letras, números o cualquier 
#                               otro signo) y se la reemplaza con una letra "desplazada". Si desplazas la letra A un espacio, 
# obtienes la letra B. Si desplazas la A dos espacios, obtienes la letra C. La Figura 14-1 es una ilustración de letras 
# desplazadas tres espacios.

# Figura 14-1: Letras desplazadas tres espacios. Aquí B se transforma en E.

# Para obtener cada letra desplazada, dibuja una fila de casilleros con cada letra del alfabeto. Luego dibuja una segunda 
# fila de casilleros debajo de ella, pero comienza un cierto número (este número es la clave) de casilleros hacia la derecha.
# Luego de la última letra, vuelve a comenzar con la primera. Aquí hay un ejemplo con las letras desplazadas tres espacios.

# Figura 14-2: El alfabeto completo desplazado tres espacios.

# El número de espacios que te desplazas es la clave en el Cifrado César. El ejemplo anterior muestra las traducciones de cada
# letra para la clave 3.

# Si encriptas el texto plano "Adios" con una clave 3, entonces:

# ·        La “A” se convierte en “D”.

# ·        La letra “d” se convierte en “g”.

# ·        La letra “i” se convierte en “l”.

# ·        La letra “o” se convierte en “r”.

# ·        La letra “s” se convierte en “v”.

# El criptograma de "Adios" con clave 3 resulta “Dglrv”.

# Los caracteres que no correspondan a letras no serán alterados. Para desencriptar "Dglrv" con la clave 3, partimos de la fila 
# inferior de casilleros y volvemos hacia arriba:

# ·        La letra “D” se convierte en “A”.

# ·        La letra “g” se convierte en “d”.

# ·        La letra “l” se convierte en “i”.

# ·        La letra “r” se convierte en “o”.

# ·        La letra “v” se convierte en “s”.



# La primera línea es simplemente un comentario. TAM_MAX_CLAVE es una constante que almacena al entero 26. 
# TAM_MAX_CLAVE nos recuerda que en este programa, la clave usada para el cifrado debe estar comprendida 
# entre 1 y 26.

TAM_MAX_CLAVE = 26

# La función obtenerModo() permite al usuario elegir si quieren entrar al modo de cifrado o descifrado del 
# programa. El valor devuelto de input() y lower() se almacena en modo. La condición de la sentencia if 
# comprueba si la cadena almacenada en modo existe en la lista devuelta por 'encriptar e desencriptar d'
# .split().

# Esta lista es ['encriptar', 'e', 'desencriptar', 'd'], pero es más fácil para el programador escribir 
# 'encriptar e desencriptar d'.split() y no tener que escribir todas esas comas y comillas. Usa la forma 
# que sea más fácil para tí; ambas son evaluadas al mismo valor de lista.

# Esta función devolverá la cadena en modo siempre que modo sea igual a 'encriptar', 'e', 'desencriptar' 
# o 'd'. Entonces, obtenerModo() devolverá la cadena 'e' o la cadena 'd' (pero el usuario puede escribir 
# “e”, “encriptar”, “d” o “desencriptar”.)

def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar o descifrar por fuerza bruta un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d bruta b'.split():
            return modo

        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d" o "bruta" o "b"')
# Este código permitirá al usuario elegir "fuerza bruta" como un modo.            
# La función obtenerMensaje() simplemente obtiene el mensaje a encriptar o desencriptar del usuario y devuelve este valor.

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

# La función obtenerClave() permite al jugador escribir la clave que desea usar para encriptar o desencriptar el mensaje. 
# El bucle while asegura que la función se mantenga ciclando hasta que el usuario ingrese una clave válida.

# Una clave válida es aquella que está comprendida entre los valores enteros 1 y 26 (recuerda que TAM_MAX_CLAVE tendrá 
# siempre el valor 26 porque es constante). La función devuelve entonces esta clave. La línea 22 establece la clave 
# como la versión entera de lo que el jugador haya escrito, de modo que obtenerClave() devuelve un entero.

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

# obtenerMensajeTraducido() realiza la encriptación y desencriptación. Tiene tres parámetros:

# ·        modo elige entre los modos de encriptación y desencriptación.

# ·        mensaje es el texto plano (o criptograma) a encriptar (o desencriptar).

# ·        clave es la clave numérica a usar para este cifrado.

# La línea 121 comprueba si la primera letra en la variable modo es la cadena 'd'. En ese caso, el programa 
# entra en modo de desencriptación. La única diferencia entre los modos de desencriptación y encriptación 
# es que para desencriptar un mensaje se usa la versión negativa de la clave. Si clave fuera el entero 22, 
# entonces en modo de desencriptación clave se transforma en -22. Explicaremos la razón de esto más adelante.

# traduccion es la cadena que contiene al resultado, es decir, el criptograma (si estás encriptando) o el 
# texto plano (si estás desencriptando). Comienza como una cadena vacía a cuyo final se van añadiendo 
# caracteres encriptados o desencriptados.


def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
    traduccion = ''
    # El bucle for de la línea 131 itera sobre cada letra (en criptografía se llaman símbolos) de la cadena del mensaje. 
    # En cada iteración sobre este bucle, simbolo tendrá el valor de una letra en el mensaje.

    # La línea 144 está presente porque sólo las letras serán encriptadas o desencriptadas. Los números, 
    # signos de puntuación y todo lo demás conservará su forma original. La variable num almacenará el 
    # valor ordinal entero de la letra en la variable simbolo. La línea 34 “desplaza” entonces el valor 
    # de num en el número de casilleros correspondiente a la clave.
    for simbolo in mensaje:
        # Los Métodos de Cadena isupper() e islower()
        # El método de cadena isalpha() devolverá True si la cadena es una letra mayúscula o minúscula 
        # entre A y Z. Si la cadena contiene algún caracter no alfabético, entonces isalpha() devolverá False

        # Los métodos de cadena isupper() e islower() (los cuales utilizamos en las líneas 147 y 152) 
        # funcionan de forma similar a los métodos isdigit() e isalpha().

        # isupper() devuelve True si la cadena sobre la cual es llamado contiene al menos una 
        # letra mayúscula y ninguna minúscula. islower() devuelve True si la cadena sobre la cual
        # es llamado contiene al menos una letra minúscula y ninguna mayúscula. De otro modo estos
        # métodos devuelven False.
        
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
            
            # La línea 157 comprueba si el símbolo es una letra mayúscula. Si lo es, hay dos casos especiales 
            # a tener en cuenta. Qué ocurriría si el símbolo fuese 'Z' y la clave 4? En este caso, el valor 
            # de num aquí sería el caracter '^' (El ordinal de '^' es 94). Pero ^ no es ninguna letra. Y 
            # nosotros queremos que el criptograma "reinicie la vuelta" por el principio del alfabeto.

            # Comprobamos si num tiene un valor mayor que el valor ordinal de “Z”. Si es así, restamos 26 
            # a num (porque hay 26 letras en total). Luego de hacer esto, el valor de num es 68. 68 es el 
            # valor ordinal correcto ya que corresponde a 'D'.
            
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
                    
            # Si el símbolo es una letra minúscula, el programa ejecuta un código que es similar a las líneas 
            # 157 a 161. la única diferencia es que utiliza ord('z') y ord('a') en lugar de ord('Z') y ord ('A').

            # En modo desencriptación, la clave es negativa. El caso especial sería si num -= 26 es menor que 
            # el valor ASCII de “a”. En ese caso, sumamos 26 a num para que “reinicie la vuelta” por el final 
            # del alfabeto.
            
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                    
            # La línea 182 concatena el caracter encriptado/desencriptado a la cadena traducida.

            # Si el símbolo no es una letra mayúscula o minúscula, la línea 185 concatena el símbolo 
            # original a la cadena traducida. Por lo tanto, espacios, números, signos de puntuación 
            # y otros caracteres no serán encriptados o desencriptados.
            
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