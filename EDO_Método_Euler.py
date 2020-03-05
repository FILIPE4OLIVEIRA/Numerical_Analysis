# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 18:49:35 2020
@author: engoliveira

"""

# Este método resolve o problema da EDO y' - 2xy = 0 ; y(1) = 1 

# Método de Euler - EDO

import numpy
import matplotlib.pyplot as plt

# Função
def g(x,y):

	return (2*x*y)

# Método de Euler
def Euler(g,x0,x1,y0):

	numb_div = 100000
	numb_int = (x1-x0)/numb_div

	x_aprox = [x0]
	y_aprox = [y0]

	for i in range(0,numb_div):

		y1 = y_aprox[i] + numb_int*g(x_aprox[i],y_aprox[i])
		x1 = x_aprox[i] + numb_int
		y_aprox.append(y1)
		x_aprox.append(x1)

	print("\n\t O Valor Aproximado da EDO no Ponto %.2f é: %.8f" %(x1,y_aprox[-1]))

	# Plotagem do Gráfico 1
	plt.figure(1)
	plt.title('Gráfico da Solução: dy/dx - 2xy = 0  ; y(1) = 1')
	plt.xlabel('EIXO X')
	plt.ylabel('EIXO Y')
	plt.plot(x_aprox,y_aprox, label = 'Solução', color = 'blue', linestyle = 'dashed')
	plt.legend()
	plt.grid()
	plt.show()
