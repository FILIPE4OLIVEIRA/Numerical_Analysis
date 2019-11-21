# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import numpy
import matplotlib.pyplot as plt

def g(x):

	return(numpy.exp(-3*x)*numpy.sin(4*x))

def integral_simples(g,x0,x1):
	random_results = []
	random_numb = 1000
	var_count = 0

	while(var_count<10000):
		SOMA1 = 0
		for x in range(random_numb):
			X = x0+(x1-x0)*numpy.random.uniform(0,1,1)
			SOMA1 += g(X)
	
		random_approximation = float((x1-x0)*(SOMA1/random_numb))
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))
    
    	#Plotagem do Gráfico de G(x)
	x = numpy.linspace(x0,x1)

	#Plotagem do Gráfico 1
	plt.figure(1)
	plt.title('Gráfico de G(x)')
	plt.xlabel('EIXO X')
	plt.ylabel('EIXO Y')
	plt.plot(x,g(x))
	plt.fill_between(x,g(x))
	plt.grid()
	plt.show()

	#Plotagem do Gráfico 2
	plt.figure(2)
	plt.title('Distribuição da Integral')
	plt.hist(random_results, bins = 30, ec = 'black')
	plt.xlabel('Valor da Integral')
	plt.ylabel('Frequência')
	plt.show()
    
	
	print("\n")

	return(print("\tA Integral Aproximada da Função é:%.8f" %(Integral)))
