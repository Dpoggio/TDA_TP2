from Arguments import *
from Huffman import *
from ComprimirYDescomprimir import *
import Constant as p

decode, archivo_frecuencia, archivo_entrada, archivo_salida = Arguments().getArgs()

huff=Huffman(archivo_frecuencia)
huff.procesarHuffman()

if not decode:
    codificar(archivo_entrada,archivo_salida,huff.getDicCodificar())
else:
    decodificar(archivo_entrada,archivo_salida,huff.getDicDecodificar())

"""
if not decode:
    print("Modo de Codificacion")
    # Genera el codigo para codificar
    h.generateCode()
    # Codificar el archivo de entrada segun el codigo generado
    h.code()
else:
    print("Modo de Decodificacion")
    # Generar el codigo para decodificar
    h.generateDecode()
    # Decodificar el archivo de entrada segun el codigo generado
    h.decode()
"""
return 0