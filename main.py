from Arguments import *
from Huffman import *
from ComprimirYDescomprimir import *
import Constant as p

decode, archivo_frecuencia, archivo_entrada, archivo_salida = Arguments().getArgs()

"""Creamos un Huffman que lee el archivo de frecuencias y procesa los datos ingresados, 
almacena dos diccionarios de codificiación y decodificacion """
huff=Huffman(archivo_frecuencia.name)
huff.procesarHuffman()

#Dependiendo de lo ingresado en teclado, llamará a la funcion codificar o decodificar
if not decode:
    codificar(archivo_entrada.name,archivo_salida.name,huff.getDicCodificar())
else:
    decodificar(archivo_entrada.name,archivo_salida.name,huff.getDicDecodificar())
