# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:46:37 2019
@author: engoliveira

"""

# Método Numérico da Secante

import math

def g(x):

	return(math.exp(-3*x)*math.sin(4*x))

def secante(g,x0,x1):
	erro = 0.0000001
	maxint = 100
	var_count = 1
	if(g(x0)*g(x1)<0):
		x2 = (x0+x1)/2
		print("\n")
		print("Iteração\t Ponto(x0)\t Ponto(x1)\t |g(x2)|")
		while(var_count<maxint and abs(g(x2))>erro):
			x2 = x1 - ((g(x1)*(x1-x0))/(g(x1)-g(x0)))
			print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,x0,x1,abs(g(x2))))
			x0 = x1
			x1 = x2
			var_count = var_count + 1
		
		if(var_count>maxint):
			print("\n")
			print("ERRO: Numero Máximo de Iterações Atingido!")
		else:
			print("\n")
			print("A raiz aproximada da função é: %.8f" %(x2))

	else:
		print("\n")
		print("Não existe raiz nesse intervalo.")
