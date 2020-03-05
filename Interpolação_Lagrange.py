# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 06:00:09 2020
@author: engoliveira

"""

# Este método interpola os dados apresentados no vetores x e y a partir do polinômio de lagrange.
# também é possível calcular o valor da interpolação em um ponto usando a variável xp.

# Interpolação de Lagrange

import numpy
import matplotlib.pyplot as plt

x = [0,20,40,60,80,100]    				# DADOS EIXO X
y = [26.0,48.6,61.6,71.2,74.8,75.2]		# DADOS EIXO Y

def Lagrange_Interpolation(x,y,xp):

	N1 = len(x) - 1

	X = numpy.linspace(x[0],x[-1],1000)
	Y = []

	# Interpolação para todos os pontos
	for k in range(len(X)):
		SOMA1  = 0
		for i in range(N1+1):
			P1 = 1
			for j in range(N1+1):
				if(j != i):
					P1 = P1 * (X[k] - x[j])/(x[i] - x[j])

			SOMA1 = SOMA1 + y[i]*P1
		Y.append(SOMA1)

	# Interpolação para um único ponto xp qualquer
	SOMA2  = 0
	for i in range(N1+1):
		P2 = 1
		for j in range(N1+1):
			if(j != i):
				P2 = P2 * (xp - x[j])/(x[i] - x[j])

		SOMA2 = SOMA2 + y[i]*P2

	print("\n O valor da Interpolação no Ponto x = %.3f é  y = %.5f" %(xp,SOMA2))

	# Plotagem dos Gráficos Observado vs Interpolação
	plt.title('Gráfico: Observado vs Interpolação')
	plt.xlabel('EIXO X')
	plt.ylabel('EIXO Y')
	plt.plot(x,y, label = 'Observado', color = 'blue', linestyle = 'solid')
	plt.plot(X,Y, label = 'Interpolação', color = 'red', linestyle = 'dashed')
	plt.legend()
	plt.grid()
	plt.show()
