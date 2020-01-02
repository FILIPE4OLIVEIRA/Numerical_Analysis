# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:49:35 2020
@author: engoliveira

"""

# Método de Euler - EDO

import numpy
import matplotlib.pyplot as plt

# Função
def g(x,y):

	return (y*numpy.sqrt(x))

# Método de Euler
def euler(g,x0,x1,y0):

	numb_div = 100000
	numb_int = (x1-x0)/numb_div

	x_aprox = [x0]
	y_aprox = [y0]

	for i in range(0,numb_div):

		y1 = y_aprox[i] + numb_int*g(x_aprox[i],y_aprox[i])
		x1 = x_aprox[i] + numb_int
		y_aprox.append(y1)
		x_aprox.append(x1)

	# Plotagem do Gráfico 1
	plt.figure(1)
	plt.title('Gráfico da Função: G(x,y(x))')
	plt.xlabel('EIXO X')
	plt.ylabel('EIXO Y')
	plt.plot(x_aprox,y_aprox)
	plt.grid()
	plt.show()

	return(print("\n\t O Valor Aproximado da EDO no Ponto %.2f é: %.8f" %(x1,y_aprox[-1])))