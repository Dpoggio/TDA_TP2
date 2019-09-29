def codificar(archivo_entrada,archivo_salida, dic_huff):
    try:
        with open(archivo_entrada) as inFile, open(archivo_salida,'w') as outFile:
            lectura = inFile.read()
            for caracter in lectura:
                outFile.write(dic_huff[caracter])
    except IOError:
        raise IOError
    

def decodificar(archivo_entrada,archivo_salida, dic_huff):
    codigo=""
    try:
        with open(archivo_entrada) as inFile, open(archivo_salida,'w') as outFile:
            lectura = inFile.read()
            for caracter in lectura:
                codigo+=caracter
                if codigo in dic_huff:
                    outFile.write(dic_huff[codigo])
                    codigo=""
    except IOError:
        raise IOError