# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""
# EDO: y' + P(x)y = 0
# Este método resolve o problema da EDO y' - 2xy = 0 ; y(0) = 1 

# Método de Runge Kutta 4° Ordem

import numpy
import matplotlib.pyplot as pyplot

# Função
def w(x,y):
	return (2*x*y)

# Método de Runge Kuttas
def Runge_Kutta_O4(w,x0,x1,y0):

	numb_div = 10000
	h = (x1-x0)/numb_div

	x_aprox = [x0]
	y_aprox = [y0]

	for i in range(numb_div):

		k1 = h*w(x_aprox[i], y_aprox[i])
		k2 = h*w(x_aprox[i] + (h/2), y_aprox[i] + k1*(h/2))
		k3 = h*w(x_aprox[i] + (h/2), y_aprox[i] + k2*(h/2))
		k4 = h*w(x_aprox[i] + h, y_aprox[i] + k3)

		y_next = y_aprox[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
		x_next = x_aprox[i] + h

		y_aprox.append(y_next)
		x_aprox.append(x_next)

	print("\nA função y(x) no ponto %.2f é aproximadamente: %.8f" %(x1,y_aprox[-1]))

	# Plotagem do Gráfico 1
	pyplot.title("Gráfico da EDO \n y' - 2xy = 0 ; y(0) = 1")
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x_aprox,y_aprox, label = 'Solução Númerica y(x)', color = 'blue', linestyle = 'dashed')
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()
