# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:27:18 2020
@author: engoliveira

"""

# Cálculo de Autovalores

import numpy
from sympy import *

A = numpy.array([[4.0,41.0,78.0],[48.0,28.0,21.0],[26.0,13.0,11.0]]) # Matriz 

def Autovalor(A):
	lenght = len(A[0])
	y = Symbol('y')
	M = Matrix(A)

	for i in range(lenght):
		for j in range(lenght):
			if(i==j):
				M[i,j] = M[i,j] - y

	detM = M.det()
	Eq = str(detM)
	autovalores = nroots(Eq, n=8)
	return(print("Autovalores: " ,(autovalores)))