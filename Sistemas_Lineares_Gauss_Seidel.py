# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:30:37 2020
@author: engoliveira

"""

# Método de Gauss-Sidel para solução de Sistemas Lineares

import numpy

A = numpy.array([[8,2,-1,0],[2,-4,0,0],[0,-2,8,-1],[0,0,-1,4]])
b = numpy.array([1,1,1,1])

def Sassenfeld(A,b):
 	coef = list(numpy.ones(len(b)))
 	for i in range(len(b)):
 		for j in range(len(b)):
 			if (i != j):
 				coef[i] = coef[i] + A[i][j]*coef[j]


 		coef[i] = coef[i]/A[i][i]

 	sf = max(coef)

 	return(sf)

def Gauss_Sidel(A,b,max_int=100):

	solution  = list(numpy.zeros(len(b)))
	vec_aprox = list(numpy.zeros(len(b)))
	real_erro = list(numpy.ones(len(b)))
	erro_alvo = list(0.0000001*numpy.ones(len(b)))

	sf = Sassenfeld(A,b)
	
	var_count = 0
	if (sf<1):
		while(real_erro > erro_alvo and var_count < max_int):
			
			for i in range(len(b)):
				SOMA1 = 0
				for j in range(len(b)):
					if(i != j):
						SOMA1 = SOMA1 + A[i,j]*vec_aprox[j]
				vec_aprox[i] = (b[i] - SOMA1)/A[i,i]


			for k in range(len(b)):
				SOMA2 = 0
				for h in range(len(b)):
					SOMA2 = SOMA2 + A[k,h]*vec_aprox[h]
					real_erro[k] = abs(SOMA2 - b[k])

			var_count = var_count + 1

		iterations = var_count
		solution = list(round(i,10) for i in vec_aprox)

		print("Número de Iterações: %.i" %var_count)
		print("Solução do Sistema Linear:",(solution))

	else:
		solution  = None
		iterations = None
		print("Método Não Converge.")

	return(solution,iterations)
