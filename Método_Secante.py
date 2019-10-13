# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:46:37 2019
@author: engoliveira

"""

# Método Numérico da Secante

import math

erro = 0.0000001
maxint = 100
var_count = 1

def function(x):

	return(math.exp(-3*x)*math.sin(4*x))

def intervalos():
	limites = []
	print("digite o intervalo de busca [x0,x1]:")
	for x in range(0,2):
		if(x == 0):
			y = float(input("digite o limite esquerdo x0: "))
			limites.append(y)
		else:
			y = float(input("digite o limite direito x1: "))
			limites.append(y)

	return(limites)

I = intervalos()

print("\n")
if(function(I[0])*function(I[1])<0):
	x2 = (I[0]+I[1])/2
	print("Iteração\t Ponto (x0)\t Ponto (x1)\t f(x2)")
	while(var_count<maxint and abs(function(x2))>erro):

		x2 = I[1] - ((function(I[1])*(I[1]-I[0]))/(function(I[1])- function(I[0])))

		print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,I[0],I[1],abs(function(x2))))

		I[0] = I[1]

		I[1] = x2

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
