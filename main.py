from Arguments import *
import Huffman
import Constant as p

modo, c_fp, in_fp, out_fp = Arguments().getArgs()
h = Huffman(c_fp, in_fp, out_fp)


if modo == p.CODE_MODE:
    # Genera el codigo para codificar
    h.generateCode()
    # Codificar el archivo de entrada segun el codigo generado
    h.code()
else:
    # Generar el codigo para decodificar
    h.generateDecode()
    # Decodificar el archivo de entrada segun el codigo generado
    h.decode()