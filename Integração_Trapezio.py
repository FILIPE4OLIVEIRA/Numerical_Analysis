# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 05:56:53 2019
@author: engoliveira

"""

# Regra do Trapezio Composta

import math

numb_breaks = 1000
SOMA1 = 0

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

step = (I[1]- I[0])/numb_breaks

for x in range(1,numb_breaks):

	SOMA1 += 2*function(I[0] + x*step)

Integral = float((step/2)*(function(I[0]) + SOMA1 + function(I[1])))

print("\n")
print("A Integral Aproximada da Função é:%.8f" %(Integral))
