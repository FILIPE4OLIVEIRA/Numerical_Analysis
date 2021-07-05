# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:30:37 2020
@author: engoliveira

"""

# Método de Eliminação de Gauss para solução de Sistemas Lineares

import numpy

A = numpy.array([[8.,2.,-1.,0],[2.,-4.,0.,0.],[0.,-2.,8.,-1.],[0.,0.,-1.,4.]])
b = numpy.array([1.,1.,1.,1.])

def Pivot_Parcial(A,b):

	for i in range(len(b)):
		Pivot_1 = numpy.abs(A[i][i])
		L_Pivot = i
		for j in range(i+1,len(b)):
			Pivot_2 = numpy.abs(A[j][i])
			if(Pivot_2>Pivot_1):
				Pivot_1 = Pivot_2
				L_Pivot = j

		if(L_Pivot != i):
			A_Aux = A[i,:].copy()
			A[i,:] = A[L_Pivot,:]
			A[L_Pivot,:] = Aux_A

			Aux_b = b[i].copy()
			b[i] = b[L_Pivot]
			b[L_Pivot] = Aux_b


	def Triangular_Superior(A,b):
		for i in range(len(b)-1):
			for j in range(i+1,len(b)):
			  	beta = A[j,i]/A[i,i]
			  	A[j,:] = A[j,:] - beta * A[i,:]
			  	b[j] = b[j] - beta * b[i]

		return(A,b)


	A1,b1 = Triangular_Superior(A,b)
	
	return(A1,b1)

def Gauss_Method(A,b):

	A2,b2 = Pivot_Parcial(A,b)

	solution = list(numpy.zeros(len(b2)))

	i = len(b2) - 1
	while(i >= 0):
		x = b2[i]
		j = len(b2)-1
		while(j > i):
			x = x - A2[i][j]*solution[j]
			j = j-1

		x = x/A2[i][i]
		i = i-1
		solution[j] = x

	return(print("Solução do Sistema Linear:",(solution)))

S = Gauss_Method(A,b)
