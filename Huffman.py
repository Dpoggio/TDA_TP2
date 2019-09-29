import heapq as he
import csv
from operator import itemgetter

class Node:
	def __init__(self, freq, char=None, left=None, right=None):
		self.freq = freq
		self.char = char
		self.left = left
		self.right = right

	def __lt__(self, other):
		if self.freq == other.freq:
			if self.char and other.char:
				return self.char < other.char
			else:
				return False
		else:
			return self.freq < other.freq	
	# def __cmp__(self, other):
	#     # if other == None:
	#     #     return -1
	# 	if not isinstance(other, Node):
	# 		return -1

	# 	return self.freq > other.freq


class Huffman:
	def __init__(self, c_fp, in_fp, out_fp):
		self.c_fp = c_fp
		self.in_fp = in_fp
		self.out_fp = out_fp
		self.code_d = {}
		self.decode_d = {}


	def dequeue(self, root, code):
		if root:
			# if root.char:
			# if root.left:
			# 	if root.right:
			# 		print(root.left.char,"<- [", root.char, "]->", root.right.char, " |", code)
			# 	else:
			# 		print(root.left.char,"<- [", root.char, "]-> ", " |", code)
			# else:
			# 	if root.right:
			# 		print(" <- [", root.char, "]->", root.right.char, " |", code)
			# 	else:
			# 		print(" <- [", root.char, "]-> ", " |", code)

			if root.char:
				self.code_d[root.char] = code
				self.decode_d[code] = root.char
			self.dequeue(root.left, code + "0")
			# print("["+"]", root.freq, code)
			self.dequeue(root.right, code + "1")

	def generateCode(self, lista):
		# Generar un diccionario con el valor del ASCII como Clave
		it = lista.split(',')
		# code = dict()
		li = []
		he.heapify(li)

		for char, freq in lista:
			n = Node(freq, char)
			he.heappush(li, n)
		
		count = 0
		
		#LO DEJAMOS ACA
		while len(li) > 1:
			left = he.heappop(li)
			# print("left: ",left.freq)
			right = he.heappop(li)
			# print("right: ",right.freq)
			# n =  Node(left.freq + right.freq, str(count), left, right)
			n =  Node(left.freq + right.freq, None, left, right)
			count = count + 1
			he.heappush(li, n)

		code = ""
		root = he.heappop(li)

		# print(li.left)
		# print(root.char)
		
		self.dequeue(root, code)
		print(self.code_d)
		print(self.decode_d)
		return

	def crearListaHuffman(self):
		#archivo = os.path.join("Archivos","test.txt")
    	listaHuffman= []
    	try:
        	with open(c_fp) as inFile:
            	lectura = inFile.read()
            	#Creo una lista de frecuencias en chars
            	l_frecuencias = lectura.split(",")
            	#Creo lista de frecuencias en numeros
            	frecuencias = list(map(int, l_frecuencias))
            	for i in range (len(frecuencias)):
                	caracter = chr(i)
                	#Guardo el chr en ascii y la frecuencia en una lista
                	listaHuffman.append((caracter, frecuencias[i]))
    	except IOError:
        	print("Error al leer el archivo")
        
        #Devuelvo una lista ordenada por el segundo item de la tupla
    	return sorted(listaHuffman, key=operator.itemgetter(1))

	def code(self):
		# Codificar cada caracter al archivo de salida
		return

	def decode(self):
		# Decodificar cada caracter al archivo de entrada
		return