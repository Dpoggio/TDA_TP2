import heapq as heap
import csv
from operator import itemgetter
import Exceptions as e
CANT_ASCII=256

class Node:
	""" Clase Nodo que permite almacenar la frecuencia de un caracter, el caracter y su hojo izquierdo y derecho """
	def __init__(self, freq, char=None, izq=None, der=None):
		self.freq = freq
		self.char = char
		self.izq = izq
		self.der = der

	def __lt__(self, other):
		""" Permite comparar el menor, utilizado en el heap de minimos """
		if self.freq == other.freq:
			if self.char and other.char:
				return self.char < other.char
			else:
				return False
		else:
			return self.freq < other.freq	

class Huffman:
	""" Clase Huffman que contiene el archivo de frecuencias, y dos hash para codificar y decodificar """
	def __init__(self, archivo_frecuencia):
		self.archivo_frecuencia = archivo_frecuencia
		self.code_dic = {}
		self.decode_dic = {}
	
	def getDicCodificar(self):
		""" Devuelve el hash para codificar """
		return self.code_dic
		
	def getDicDecodificar(self):
		""" Devuelve el hash para decodificar"""
		return self.decode_dic

	def generarCodigo(self, raiz, codigo):
		""" Función encargada de crear los hash para codificar y decodificar a partir del arbol de Huffman """
		if raiz:
			if raiz.char:
				self.code_dic[raiz.char] = codigo
				self.decode_dic[codigo] = raiz.char
			self.generarCodigo(raiz.izq, codigo + "0")
			self.generarCodigo(raiz.der, codigo + "1")
				
	def procesarHuffman(self):
		"""Función principal de Huffman que llama a la función para crear la lista de tuplas (caracter,frecuencia),
			arma el arbol de huffman, y finalmente llama a la función encargado de crear los hash para codificar y decodificar """
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
			der = heap.heappop(listaHeapify)

			nodo =  Node(izq.freq + der.freq, None, izq, der)
			heap.heappush(listaHeapify, nodo)

		codigoHuffman = ""
		raiz = heap.heappop(listaHeapify)		
		self.generarCodigo(raiz, codigoHuffman)
	

	def crearListaHuffman(self):
		""" Función encargaga de crear la lista de tuplas (caracter, frecuencia) para procesar Huffman """
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
					caracter = chr(i)
					#Guardo el char en ascii y la frecuencia en una lista
					listaHuffman.append((caracter, frecuencias[i]))
			return listaHuffman
		
		except IOError:
			raise IOError
		except ValueError:
			raise ValueError