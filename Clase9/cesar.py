
from os import system

miAlfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# En base a la posición de una letra, sumarle 3 y reemplazar


totalAlfabeto = int(len(miAlfabeto))
system("clear")
myStringEncriptado = ""

myString = input("Ingrese la palabra a encriptar ")

for letra in myString:

    
    for i in range(totalAlfabeto):
        
        if letra == miAlfabeto[i]:
            myStringEncriptado = myStringEncriptado + miAlfabeto[i+3]

print("Palabra encriptada: "+myStringEncriptado)