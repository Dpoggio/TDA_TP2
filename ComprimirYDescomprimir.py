def codificar(archivo_entrada,archivo_salida, dic_huff):
    """ Funcion codificar que recibe un archivo de entrada, un hash de huffman y un archivo de salida.
        Lee el archivo de entrada y por cada caracter lo codificamos con el hash de huffman, posteriormente
        lo escribe en el archivo de salida. """
    try:
        with open(archivo_entrada) as inFile, open(archivo_salida,'w') as outFile:
            lectura = inFile.read()
            for caracter in lectura:
                outFile.write(dic_huff[caracter])
    except IOError:
        raise IOError
    

def decodificar(archivo_entrada,archivo_salida, dic_huff):
    """ Funcion decodificar que recibe un archivo de entrada, un hash de huffman y un archivo de salida.
        Lee el archivo de entrada y por cada conjunto de bits que se encuentra en el hash de huffman lo decodifica, posteriormente
        lo escribe en el archivo de salida. """
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