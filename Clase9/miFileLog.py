# Crear un archivo txt y lo que se imprime se guarda en el archivo

def printLog(log, stringLog):
    log.write(stringLog+"\n")


try:
    log = open("./Clase9/Log/fileLog", 'w')
    printLog(log, "Prueba2")
    log.close   
    
except Exception as err:
    print("Se generó un Error "+str(type(err)))
    log.close