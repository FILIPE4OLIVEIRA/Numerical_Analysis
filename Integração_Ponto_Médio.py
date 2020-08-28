# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:14:09 2019
@author: engoliveira

"""

# Regra do Ponto Médio

import numpy
import matplotlib.pyplot as pyplot

def g(x):

	return(1/2 + 3*x*numpy.exp(-x**2))

def Ponto_Medio(g,x0=-2,x1=2):

	numb_breaks = 100000
	SOMA1 = 0
	step = (x1-x0)/numb_breaks

	for x in range(0,int((numb_breaks/2))):

		SOMA1 += g(x0 + 2*(x+1)*step)

	Integral = float(2*step*SOMA1)

	#Plotagem do Gráfico de G(x)
	xt = numpy.linspace(x0,x1,1000)

	pyplot.title('Gráfico de g(x)')
	pyplot.plot(xt,g(xt), color = "black", label = "$g(x) = 1/2 + 3xe^{-x^2}$")
	pyplot.fill_between(xt,g(xt), where = g(xt) >= 0, color = "green", interpolate = True, alpha = 0.3 , hatch = "///")
	pyplot.fill_between(xt,g(xt), where = g(xt) <= 0, color = "red", interpolate = True,  alpha = 0.3 , hatch = "///")
	pyplot.text(x = -2.0, y = 1.02, s = "Área Aproximada = %.8f" %(Integral))
	pyplot.legend(loc = 'upper left')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()

	print("\n")
	return(print("\tA Integral Aproximada da Função é: %.8f" % (Integral)))
