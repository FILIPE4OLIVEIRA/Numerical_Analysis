# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import math
import numpy

def g(x):

	return(math.exp(-3*x)*math.sin(4*x))

def monte_carlo(g,x0,x1):
	random_results = []
	random_numb = 1000
	var_count = 0

	while(var_count<100):
		SOMA1 = 0
		for x in range(random_numb):

			SOMA1 += g(x0+(x1-x0)*numpy.random.uniform(0,1,1))
	
		random_approximation = float(((x1-x0)/random_numb)*SOMA1)
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))
	print("\n")
	return(print("\tA Integral Aproximada da Função é:%.8f" %(Integral)))
