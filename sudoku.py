# -*- coding: utf-8 -*-
"""sudoku.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ykZ_x1AOQJARzDluuF79vRYP_qBAkbbh
"""

import numpy as np
import random

flag = False
pos = []

def printMatrix(matrix):
  cont = 0#contador para divisor vertical
  print('—————————————————————————')
  for i, fila in enumerate(matrix):
    print('| ', end="")
    for elemento in fila:
        if(elemento == 0):
          elemento = " "

        print(elemento, end=" ")
        cont+=1
        if(cont==3):#validacion para poner el divisor
          print('| ', end="")
          cont=0
    print()
    if(i==2 or i==5 or i==8):
      print('—————————————————————————', end="")
      print()

def validarTablero(tablero, fila, col, num):
  if (fila, col) in pos:#si son los numeros generados
    if(flag):
      print("No puede modificar este número, puesto que ya está dado")
    return False

  if num in tablero[fila,:]:#si se repite en la fila
    if(flag):
      print("El número está repetido en la fila")
    return False

  if num in tablero[:,col]:#si se repite en la columna
    if(flag):
      print("El número está repetido en la columna")
    return False

  frow = 3 * (fila // 3) #devuelve el indice de la primera fila en la cajita
  fcol = 3 * (col // 3)#devuelve el indice de la primera columna de la cajita

  if num in tablero[frow:frow+3, fcol:fcol+3]:#si se repite en la cajita
    if(flag):
      print("El número está repetido en la cajita")
    return False

  return True

def buscarCeldaV(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila, col] == 0:
                return fila, col
    return None

def generarTablero(solucion):
    pos = buscarCeldaV(solucion)
    if not pos:
        return True

    fila, col = pos

    for i in range(9):
      num = random.randint(1,9)
      if validarTablero(solucion, fila, col, num):
          solucion[fila, col] = num

          if generarTablero(solucion):
              return True

          solucion[fila, col] = 0

    return False

solucion = np.zeros((9, 9), dtype=int)
tablero = np.zeros((9, 9), dtype=int)

generarTablero(solucion)
numMostrados = random.randint(20, 30)#me da la cantidad de numeros visibles en el tablero

#mostrar solo unos numeros de la solucion
for i in range(numMostrados):
  fila = random.randint(0,8)
  col = random.randint(0,8)

  while (tablero[fila, col] != 0):
    fila = random.randint(0,8)
    col = random.randint(0,8)

  pos.append((fila,col))
  tablero[fila,col] = solucion[fila,col]

flag = True
while(0 in tablero):
  printMatrix(tablero)
  texto = input("Ingrese [fila, columna, dígito]: ")
  array = texto.split(",")
  comando = [int(numero) for numero in array]

  while (not validarTablero(tablero, comando[0], comando[1], comando[2])):
    texto = input("Ingrese [fila, columna, dígito]: ")
    array = texto.split(",")
    comando = [int(numero) for numero in array]

  tablero[comando[0], comando[1]] = comando[2]

