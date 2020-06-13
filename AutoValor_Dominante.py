# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:49:35 2020
@author: engoliveira

"""

# Método da Potência para Autovalores e Autovetores

import numpy


A = numpy.array([[4,-1,1],[-1,3,-2],[1,-2,3]])
x0 = [1,1,1]

AutoValor_Aprox = []
AutoVetor_Aprox = []

def AutoValor_Dominante(A,x0):
	x_Vetor = [x0]
	x_New = []
	for j in range(10):
		yi = A.dot(x_Vetor[j])
		x_Vetor.append(yi)
		
	AutoValor = x_Vetor[-1][0]/x_Vetor[-2][0]
	AutoVetor = x_Vetor[-1]/x_Vetor[-1][0]

	AutoValor_Aprox.append(AutoValor)
	AutoVetor_Aprox.append(AutoVetor)

	print("AutoValor Aproximado: %.8f" %(AutoValor_Aprox[0]))
	print("AutoVetor Aproximado:", str(list(AutoVetor_Aprox[0])))
