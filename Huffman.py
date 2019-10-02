import heapq as heap
import csv
from operator import itemgetter
import Exceptions as e
CANT_ASCII=256

class Node:
	def __init__(self, freq, char=None, izq=None, der=None):
		self.freq = freq
		self.char = char
		self.izq = izq
		self.der = der

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
	def __init__(self, archivo_frecuencia):
		self.archivo_frecuencia = archivo_frecuencia
		self.code_dic = {}
		self.decode_dic = {}
	
	def getDicCodificar(self):
		return self.code_dic
		
	def getDicDecodificar(self):
		return self.decode_dic

	def generarCodigo(self, raiz, codigo):
		if raiz:
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

			if raiz.char:
				self.code_dic[raiz.char] = codigo
				self.decode_dic[codigo] = raiz.char
			self.generarCodigo(raiz.izq, codigo + "0")
			# print("["+"]", root.freq, code)
			self.generarCodigo(raiz.der, codigo + "1")
		#else: 
			#print(codigo)

		
	def procesarHuffman(self):
		#Creo la lista de Hufmman previa a recorrer
		try:
			listaHuffman=self.crearListaHuffman()
			
		except IOError:
			raise IOError
		except ValueError:
			raise ValueError

		listaHeapify = []
		heap.heapify(listaHeapify)

		for char, freq in listaHuffman:
			nodo = Node(freq, char)
			heap.heappush(listaHeapify, nodo)
		
		while len(listaHeapify) > 1:
			izq = heap.heappop(listaHeapify)
			# print("left: ",left.freq)
			der = heap.heappop(listaHeapify)
			# print("right: ",right.freq)
			# n =  Node(left.freq + right.freq, str(count), left, right)
			nodo =  Node(izq.freq + der.freq, None, izq, der)
			heap.heappush(listaHeapify, nodo)

		codigoHuffman = ""
		raiz = heap.heappop(listaHeapify)

		# print(li.left)
		# print(root.char)
		
		self.generarCodigo(raiz, codigoHuffman)
		#print(self.code_dic)
		#print(self.decode_dic)

	def crearListaHuffman(self):
		
		listaHuffman= []
		try:
			with open(self.archivo_frecuencia) as inFile:
				lectura = inFile.read()
				#Creo una lista de frecuencias en chars
				l_frecuencias = lectura.split(",")
				
				if len(l_frecuencias) != CANT_ASCII:
					raise e.CustomException('Error: Archivo de frecuencias incorrecto!')
					
				#Creo lista de frecuencias en numeros
				frecuencias = list(map(int, l_frecuencias))
				for i in range (len(frecuencias)):
					"""
					if frecuencias[i] != 0:
						caracter = chr(i)
						#Guardo el char en ascii y la frecuencia en una lista
						listaHuffman.append((caracter, frecuencias[i]))
					"""
					caracter = chr(i)
					#Guardo el char en ascii y la frecuencia en una lista
					listaHuffman.append((caracter, frecuencias[i]))
			#Devuelvo una lista ordenada por el segundo item de la tupla
			return listaHuffman
		
		except IOError:
			raise IOError
		except ValueError:
			raise ValueError