# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:14:09 2019
@author: engoliveira

"""

# Regra do Ponto Médio

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

for x in range(0,int((numb_breaks/2))):

	SOMA1 += function(I[0] + 2*(x+1)*step)

Integral = float(2*step*SOMA1)

print("\n")
print("A Integral Aproximada da Função é:%.8f" %(Integral))
