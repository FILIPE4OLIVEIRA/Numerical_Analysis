# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 06:49:32 2019
@author: engoliveira

"""

# Regra de Simpson Composta

import numpy
import matplotlib.pyplot as pyplot

def g(x):

	return(1/2 + x*numpy.exp(-x**2))

def Simpson(g,x0,x1):

	numb_breaks = 1000
	SOMA1 = 0
	SOMA2 = 0
	step = (x1-x0)/numb_breaks

	for x in range(1,int((numb_breaks/2)-1)):

		SOMA1 += 2*g(x0 + 2*x*step)

	for x in range(1,int((numb_breaks/2))):

		SOMA2 += 4*g(x0 + 2*(x-1)*step)

	Integral = float((step/3)*(g(x0) + SOMA1 + SOMA2 + g(x1)))

	
    #Plotagem do Gráfico de G(x)
	xt = numpy.linspace(x0,x1)

	pyplot.title('Gráfico de g(x)')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(xt,g(xt), color = "red", label = "g(x) = 1/2 + xe^(-x²)")
	pyplot.fill_between(xt,g(xt), color = "gray")
	pyplot.text(x = x1*0.30, y = x1*0.10, s = "Área Aproximada = %.8f" %(Integral))
	pyplot.legend(loc = 'upper left')
	pyplot.grid()
	pyplot.show()
	
	print("\n")
	return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))
