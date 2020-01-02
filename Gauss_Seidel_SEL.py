# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:30:37 2020
@author: engoliveira

"""

# Método de Gauss-Sidel para solução de Sistemas Lineares

import numpy

matrix = numpy.array([[3.0,-0.1,-0.2],[0.1,7.0,-0.3],[0.3,-0.2,10.0]])
vec_b = numpy.array([7.85,-19.3,71.4])

def gauss_sidel(matrix,vec_b,max_int):

	vec_aprox = numpy.zeros(3)
	var_count = 0
	solution = []
	erro = [1,1,1]

	while(var_count < max_int):
		for i in range(0,3):
			SOMA1 = 0
			for j in range(0,3):
				if(i != j):
					SOMA1 = SOMA1 + matrix[i,j]*vec_aprox[j]
			vec_aprox[i] = (vec_b[i] - SOMA1)/matrix[i,i]


		for k in range(0,3):
			SOMA2 = 0
			for h in range(0,3):
				SOMA2 = SOMA2 + matrix[k,h]*vec_aprox[h]
				erro[k] = abs(SOMA2 - vec_b[k])
				if(numpy.mean(erro) < 0.00001):
					var_count = max_int

		var_count = var_count + 1

	solution = list(vec_aprox)

	return(print("\n\t O Valor Aproximado do Vetor Solução é:",(solution)))