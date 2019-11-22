# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 05:56:53 2019
@author: engoliveira

"""

# Regra do Trapezio Composta

import numpy
import matplotlib.pyplot as plt

def g(x):

	return(numpy.exp(-3*x)*numpy.sin(4*x))

def trapezio(g,x0,x1):
	numb_breaks = 1000
	SOMA1 = 0
	step = (x1-x0)/numb_breaks

	for x in range(1,numb_breaks):

		SOMA1 += 2*g(x0 + x*step)

	Integral = float((step/2)*(g(x0) + SOMA1 + g(x1)))

	#Plotagem do Gráfico de G(x)
	x = numpy.linspace(x0,x1)

	plt.title('Gráfico de g(x)')
	plt.xlabel('EIXO X')
	plt.ylabel('EIXO Y')
	plt.plot(x,g(x))
	plt.fill_between(x,g(x))
	plt.grid()
	plt.show()

	print("\n")
	return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))
