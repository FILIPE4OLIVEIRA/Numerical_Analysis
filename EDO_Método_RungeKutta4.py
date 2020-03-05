# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""

# Este método resolve o problema da EDO y' - 2xy = 0 ; y(1) = 1 

# Método de Runge Kutta 4° Ordem

import numpy
import matplotlib.pyplot as plt

# Função
def g(x,y):

	return (2*x*y)

# Método de Runge Kutta
def RungeKutta4(g,x0,x1,y0):

	numb_div = 10000
	numb_int = (x1-x0)/numb_div

	x_aprox = [x0]
	y_aprox = [y0]

	for i in range(0,numb_div):

		k1 = g(x_aprox[i],y_aprox[i])
		k2 = g(x_aprox[i] + (numb_int/2),y_aprox[i] + k1*(numb_int/2))
		k3 = g(x_aprox[i] + (numb_int/2),y_aprox[i] + k2*(numb_int/2))
		k4 = g(x_aprox[i] + numb_int,y_aprox[i] + k3*numb_int)

		K = (1/6)*(k1 + 2*k2 + 2*k3 + k4)

		y1 = y_aprox[i] + numb_int*K
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
