from Arguments import *
from Huffman import *
import Constant as p

decode, c_fp, in_fp, out_fp = Arguments().getArgs()
h = Huffman(c_fp, in_fp, out_fp)


PARA MI ESTO NO VA, EL CODIGO DE HUFMMAN LO QUE HACE ES COMPRIME y DECODIFICA

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
