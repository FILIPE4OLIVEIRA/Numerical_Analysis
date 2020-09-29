# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:30:37 2020
@author: engoliveira

"""

# Método de Gauss-Sidel para solução de Sistemas Lineares

import numpy

matrix = numpy.array([[3.0,-0.1,-0.2],[0.1,7.0,-0.3],[0.3,-0.2,10.0]])
vec_b = numpy.array([7.85,-19.3,71.4])

def Gauss_Sidel(matrix,vec_b,max_int=100):

	solution  = [0,0,0]
	vec_aprox = [0,0,0]
	real_erro = [1,1,1]
	erro_alvo = [0.00001,0.00001,0.00001]
	
	var_count = 0
	while(real_erro > erro_alvo and var_count < max_int):
		
		for i in range(len(vec_b)):
			SOMA1 = 0
			for j in range(len(vec_b)):
				if(i != j):
					SOMA1 = SOMA1 + matrix[i,j]*vec_aprox[j]
			vec_aprox[i] = (vec_b[i] - SOMA1)/matrix[i,i]


		for k in range(len(vec_b)):
			SOMA2 = 0
			for h in range(len(vec_b)):
				SOMA2 = SOMA2 + matrix[k,h]*vec_aprox[h]
				real_erro[k] = abs(SOMA2 - vec_b[k])

		var_count = var_count + 1

	solution = list(round(i,10) for i in vec_aprox)

	print("Número de Iterações: %.i" %var_count)

	return(print("Solução do Sistema Linear:",(solution)))
