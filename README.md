# Teoria de Algoritmos - Trabajo Practico 2 - Codificacion Huffman

## Uso del programa:

Ver ayuda:

<pre><code>main.py -h
main.py --help
</code></pre>

Ejecucion:

<pre><code>main.py [-m [M]] -c file -i file -o file 
</code></pre>

  * -m , --mode : Modo de operacion. [0: Codificar, 1: Decodificar]. Default=0
  * -c , --code : Archivo de Codificacion
  * -i , --input : Archivo de Entrada
  * -o , --output : Archivo de Salida

Ejemplos: 

<pre><code>main.py -c code.txt -i text.txt -o coded_text.txt
main.py -m 1 -c code.txt -i coded_text.txt -o decoded_text.txt
</code></pre>
