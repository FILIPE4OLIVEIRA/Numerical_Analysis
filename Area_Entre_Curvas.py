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

def r(x):
	return(f(x) - g(x))

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

	#Plotagem do Gráfico
	xt = numpy.linspace(x0,x1)

	for i in range(len(xt)):
		if(r(xt[i]) >= 0.0001):
			X = xt[i]
			Y = f(xt[i])
			break

	pyplot.title('Gráfico de Área entre f(x) e g(x)')
	pyplot.plot(xt,f(xt), color = "red" , label = "$f(x) = -x^2 + 18x - 17$")
	pyplot.plot(xt,g(xt), color = "blue", label = "$g(x) = 2x + 5$")
	pyplot.plot(X,Y, marker = ".", color = "black", markersize = 8)
	pyplot.fill_between(xt,f(xt),g(xt), color = "green", alpha = 0.3 , hatch = "///")
	pyplot.text(x = X + 0.65, y = Y - 7.45, s = "Área Aproximada = %.8f" %(Area))
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5, drawstyle = 'steps')
	pyplot.show()

	print("\n")
	return(print("A Área Aproximada Entre às Funções é: %.8f" %(Area)))
