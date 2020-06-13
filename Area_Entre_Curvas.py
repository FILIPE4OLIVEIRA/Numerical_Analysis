# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 06:49:32 2019
@author: engoliveira

"""

# Área entre 2 Curvas

import numpy
import matplotlib.pyplot as pyplot

def f(x):

	return(-x**2 + 18*x -17)

def g(x):

	return(2*x + 5)

def Area_Entre_Curvas(f,g,x0=-4,x1=12):

	numb_breaks = 1000
	SOMA_F1 = 0
	SOMA_G1 = 0
	SOMA_F2 = 0
	SOMA_G2 = 0
	step = (x1-x0)/numb_breaks

	for x in range(1,int((numb_breaks/2)-1)):

		SOMA_F1 += 2*f(x0 + 2*x*step)
		SOMA_G1 += 2*g(x0 + 2*x*step)

	for x in range(1,int((numb_breaks/2))):

		SOMA_F2 += 4*f(x0 + 2*(x-1)*step)
		SOMA_G2 += 4*g(x0 + 2*(x-1)*step)

	Integral_F = float((step/3)*(f(x0) + SOMA_F1 + SOMA_F2 + f(x1)))
	Integral_G = float((step/3)*(g(x0) + SOMA_G1 + SOMA_G2 + g(x1)))

	Area = Integral_F - Integral_G

	#Plotagem do Gráfico de G(x)
	xt = numpy.linspace(x0,x1)

	pyplot.title('Gráfico de Área entre f(x) e g(x)')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(xt,f(xt), color = "red" , label = "f(x) = -x² + 18x - 17")
	pyplot.plot(xt,g(xt), color = "blue", label = "g(x) = 2x + 5")
	pyplot.fill_between(xt,f(xt),g(xt), color = "gray", hatch = "/")
	pyplot.text(x = x1*0.15, y = -x1*0.75, s = "Área Aproximada = %.8f" %(Area))
	pyplot.legend(loc = 'upper left')
	pyplot.grid()
	pyplot.show()

	print("\n")
	return(print("\tA Integral Aproximada da Função é: %.8f" %(Area)))
