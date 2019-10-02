# Teoria de Algoritmos - Trabajo Practico 2 - Codificacion Huffman

## Uso del programa:

Ver ayuda:

<pre><code>main.py -h
main.py --help
</code></pre>

Ejecucion:

<pre><code>main.py [-d] -c file -i file -o file 
</code></pre>

  * -d , --decode : Modo de Decodificacion
  * -c , --code : Archivo de Codificacion
  * -i , --input : Archivo de Entrada
  * -o , --output : Archivo de Salida

Ejemplos: 

<pre><code>python main.py -c code.txt -i text.txt -o coded_text.txt
python main.py -d -c code.txt -i coded_text.txt -o decoded_text.txt
</code></pre>


## Codigo Auxiliar generateFreq.py

Este archivo sirve para generar un archivo de codigos. El modo de ejecucion es:

<pre><code>python generateFreq.py</code></pre>

El programa buscara aquel archivo nombrado "text.txt" y generará un archivo de salida "code.txt"
