# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:27:18 2020
@author: engoliveira

"""

# Cálculo de Autovalores

import numpy
from sympy import *

A = numpy.array([[4,-1,1],[-1,3,-2],[1,-2,3]])

def AutoValores(A):
	lenght = len(A[0])
	y = Symbol('y')
	M = Matrix(A)

	for i in range(lenght):
		for j in range(lenght):
			if(i==j):
				M[i,j] = M[i,j] - y

	detM = M.det()
	Equation = str(detM)
	AutoValores = nroots(Equation, n=5)
	return(print("Autovalores: " ,(AutoValores)))
