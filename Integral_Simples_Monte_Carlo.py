# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 06:14:52 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import numpy
import matplotlib.pyplot as pyplot

def y(x):

	return(1/2 + 3*x*numpy.exp(-x**2))

def Integral_Simples(y,x0=-2,x1=2):
	random_results = []
	random_numb = 1000
	var_count = 0

	while(var_count<15000):
		SOMA1 = 0
		for i in range(random_numb):
			X = x0 + (x1-x0)*numpy.random.uniform(0,1,1)
			SOMA1 += y(X)
	
		random_approximation = float((x1-x0)*(SOMA1/random_numb))
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))
    
    #Plotagem do Gráfico de G(x)
	xt = numpy.linspace(x0,x1,1000)

	#Plotagem do Gráfico 1
	pyplot.figure(1)
	pyplot.title('Gráfico de y(x)')
	pyplot.plot(xt,y(xt), color = "black", label = "$y(x) = 1/2 + 3xe^{-x^2}$")
	pyplot.fill_between(xt,y(xt), where = y(xt) >= 0, color = "green", interpolate = True, alpha = 0.3 , hatch = "///")
	pyplot.fill_between(xt,y(xt), where = y(xt) <= 0, color = "red", interpolate = True,  alpha = 0.3 , hatch = "///")
	pyplot.text(x = -2.0, y = 1.02, s = "Área Aproximada = %.8f" %(Integral))
	pyplot.legend(loc = 'upper left')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()

	#Plotagem do Gráfico 2
	pyplot.figure(2)
	pyplot.title('Distribuição Normal dos Resultados da Integral')
	pyplot.hist(random_results, bins = 30, ec = 'black')
	pyplot.xlabel('Valor Médio da Integral')
	pyplot.ylabel('Frequência')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()
    
	
	print("\n")
	return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))
