# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import math
import numpy

random_results = []
random_numb = 10000
var_count = 0

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

while(var_count<1000):
	SOMA1 = 0
	for x in range(random_numb):

		SOMA1 += function(I[0]+(I[1]-I[0])*numpy.random.uniform(0,1,1))
	
	random_approximation = float(((I[1]-I[0])/random_numb)*SOMA1)
	random_results.append(random_approximation)
	var_count = var_count + 1


Integral = float(numpy.mean(random_results))

print("\n")
print("A Integral Aproximada da Função é:%.8f" %(Integral))

