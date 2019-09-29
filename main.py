from Arguments import *
from Huffman import *
import Constant as p

decode, c_fp, in_fp, out_fp = Arguments().getArgs()
huffman = Huffman(in_fp, out_fp)


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