
#enconding: utf-8

import csv
from pickle import TRUE
from googlesearch import search
from time import sleep
from datetime import datetime

startNow = datetime.now()
print('.\n.\n.')
print("Inicio de ejecución =", startNow)
print('.\n.\n.\nProcesando...')
# Leer un archivo Fuente
# Nombre del archivo fuente
archivo_fuente = 'LISTA-PERSONAS-A-BUSCAR.csv'

# Nombre del archivo destino
archivo_destino = 'LISTA-PERSONAS-ENCONTRADAS.csv'

with open(archivo_fuente) as archivo:

    #Omitir el encabezado
    next(archivo,None)

    # Contador de líneas
    i = 0

    # Recorrer las lineas del csv
    for linea in archivo:
        #Contador de líneas
        i = i + 1

        # Mostrar Linea 
        linea.rstrip() #.rtrip() elimina el salto de línea que se forma.

        #Convertir la línea en un arreglo con split()
        lista = linea.split(",")

        # Extraer valores de la primera columna
        ## nombre = lista[0]


        # Extraer los valores de la segunda Columna
        busqueda_google = lista[0].rstrip()
        # print(busqueda_google,'Borrar')

        # Contador búsquedas de google
        j = 0

        # Número de búsquedas en google
        nro_bus_google = 6

        #Objeto de búsquedas
        obj_bus_google = []

        # Recorrer las búsquedas de google
        for res in search(busqueda_google , num_results = nro_bus_google):
            
            # Incrementar contador
            j = j + 1

            # Eliminar el salto de Línea
            res.rstrip()
            
            # Convertir en un arreglo
            resultado = res.split(",")
            
            # Convertirlo en un String
            url_encontrada = str(resultado)
            
            # usar replace de python para eliminar caracteres
            url = url_encontrada.replace("'","").replace("[","").replace("]","")
            
            
            if "linkedin.com/company/" in url:
                """print(url, "Link valido?")"""
                obj_bus_google.append(url)
                    
            else:
                """print(" Link No válido" ,j)"""
                url = "-"
                obj_bus_google.append(url)

            # Retardo del ciclo que cada enlace encontrado
            sleep(1)

        # Termina el for de la búsqueda

        # Selecciona la url ya validada
        for e in obj_bus_google:
            if e != "-":
                url = e
            continue
        
        # Imprimir el resultado esperado
        ## print(nombre,' , ',busqueda_google,' , ',resultado[0])
        ## Imprime el index de la lista - No funciono
        print('procesada línea: ',i)

        # Crear el arreglo linkExtraidos
        linkExtraidos = [ busqueda_google , url ]
 
        #Escribir en la tercera columna en el archivo fuente 'a' ayuda a sobreescribir el archivo
        myFile = open(archivo_destino,'a')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerow(linkExtraidos)
        
        # Termina la escritura del archivo

        # Retardo del ciclo que cada búsqueda
        sleep(10)
        # print('...Fila procesada...')

print('.\n.\n.') 
endNow = datetime.now()
print("Fin de la ejecución =", endNow)
print('.\n.\n.')   

    






