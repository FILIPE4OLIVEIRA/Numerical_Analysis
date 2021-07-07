# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:49:35 2020
@author: engoliveira

"""
# EDO: y' = P(x)y

# Este método resolve o problema da EDO y' = 2xy ; y(0) = 1  

# Método de Euler - EDO

import numpy
import matplotlib.pyplot as pyplot

# Função
def P(x,y):

	return (2*x*y)

# Método de Euler
def Euler_Method(x0,x1,y0,N=50000):

	h = (x1-x0)/N

	x_aprox = [x0]
	y_aprox = [y0]

	for i in range(N):

		y_next = y_aprox[i] + h*P(x_aprox[i],y_aprox[i])
		x_next = x_aprox[i] + h

		y_aprox.append(y_next)
		x_aprox.append(x_next)

	print("\nA função y(x) no ponto %.2f é aproximadamente: %.8f" %(x1,y_aprox[-1]))

	# Plotagem do Gráfico 1
	pyplot.title("Gráfico da Solução:\n y' - 2xy = 0 ; y(0) = 1")
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x_aprox,y_aprox, label = 'Solução', color = 'red', linestyle = 'dashed')
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()
