# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""
# EDO: y' = P(x)y

# Este método resolve o problema da EDO y' = 2xy  ; y(0) = 1 

# Método de Runge Kutta 4° Ordem

import numpy
import matplotlib.pyplot as pyplot

# Função
def P(x,y):
	return (2*x*y)

# Método de Runge Kuttas
def Runge_Kutta_O4(x0,x1,y0,N=50000):

	h = (x1-x0)/N

	x_aprox = [x0]
	y_aprox = [y0]
	dydx_aprox = [0]
	dydx_exact = [0]

	for i in range(N):

		k1 = h*P(x_aprox[i], y_aprox[i])
		k2 = h*P(x_aprox[i] + (h/2), y_aprox[i] + k1*(h/2))
		k3 = h*P(x_aprox[i] + (h/2), y_aprox[i] + k2*(h/2))
		k4 = h*P(x_aprox[i] + h, y_aprox[i] + k3)

		y_next = y_aprox[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
		x_next = x_aprox[i] + h

		y_aprox.append(y_next)
		x_aprox.append(x_next)
		dydx_aprox.append(2*x_aprox[i-1]*y_aprox[i-1])

	for i in range(N):
		dydx_exact.append((2*x_aprox[i])*(numpy.exp(x_aprox[i]**2)))


	print("\nA função y(x) no ponto %.2f é aproximadamente: %.8f" %(x1,y_aprox[-1]))

	# Plotagem do Gráfico 1
	pyplot.title("Gráfico da Solução Númerica:\n y' - 2xy = 0 ; y(0) = 1")
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x_aprox,y_aprox, label = "y(x)", color = 'blue', linestyle = 'dashed')
	pyplot.plot(x_aprox,dydx_aprox, label = "y'(x)", color = 'red', linestyle = 'dashed')
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()
