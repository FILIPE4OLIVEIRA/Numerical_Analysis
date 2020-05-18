# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import numpy
import matplotlib.pyplot as pyplot

def g(x):

	return(1/2 + x*numpy.exp(-x**2))

def Integral_Simples(g,x0,x1):
	random_results = []
	random_numb = 100
	var_count = 0

	while(var_count<150):
		SOMA1 = 0
		for x in range(random_numb):
			X = x0+(x1-x0)*numpy.random.uniform(0,1,1)
			SOMA1 += g(X)
	
		random_approximation = float((x1-x0)*(SOMA1/random_numb))
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))
    
    #Plotagem do Gráfico de G(x)
	xt = numpy.linspace(x0,x1)

	#Plotagem do Gráfico 1
	pyplot.title('Gráfico de g(x)')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(xt,g(xt), color = "red", label = "g(x) = 1/2 + xe^(-x²)")
	pyplot.fill_between(xt,g(xt), color = "gray")
	pyplot.text(x = x1*0.30, y = x1*0.10, s = "Área Aproximada = %.8f" %(Integral))
	pyplot.legend(loc = 'upper left')
	pyplot.grid()
	pyplot.show()

	#Plotagem do Gráfico 2
	pyplot.figure(2)
	pyplot.title('Distribuição Normal dos Resultados da Integral')
	pyplot.hist(random_results, bins = 30, ec = 'black')
	pyplot.xlabel('Valor Médio da Integral')
	pyplot.ylabel('Frequência')
	pyplot.grid()
	pyplot.show()
    
	
	print("\n")

	return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))
