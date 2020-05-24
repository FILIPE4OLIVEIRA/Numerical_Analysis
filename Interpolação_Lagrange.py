# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 06:00:09 2020
@author: engoliveira

"""

# Este método interpola os dados apresentados no vetores x e y a partir do polinômio de lagrange.
# Também é possível calcular o valor da interpolação em um ponto usando a variável xp.

# Interpolação de Lagrange

import numpy
import matplotlib.pyplot as pyplot

x = [0.0, 0.05263157894736842, 0.10526315789473684, 0.15789473684210525, 0.21052631578947367, 0.2631578947368421, 0.3157894736842105, 0.3684210526315789, 0.42105263157894735, 0.47368421052631576, 0.5263157894736842, 0.5789473684210527, 0.631578947368421, 0.6842105263157894, 0.7368421052631579, 0.7894736842105263, 0.8421052631578947, 0.894736842105263, 0.9473684210526315, 1.0]
y = [0.5880155894689583, 0.29251170796360954, 0.04216802960693024, -0.16284262426583354, -0.32242079419418695, -0.4366825453599326, -0.5060972508142302, -0.5316133533536593, -0.5147630848145056, -0.45773652707824, -0.3634158654082591, -0.2353624092975262, -0.07775199407741502, 0.10474141349588505, 0.3071090688280594, 0.5242076923102151, 0.75098181833447, 0.9826900586951484, 1.215115667946981, 1.4447427961138775]

def Lagrange(x,y,xp):

	N1 = len(x)

	X = numpy.linspace(x[0],x[-1],N1)
	Y = []

	# Interpolação para todos os pontos
	for k in range(len(X)):
		SOMA1  = 0
		for i in range(N1):
			P1 = 1
			for j in range(N1):
				if(j != i):
					P1 = P1 * (X[k] - x[j])/(x[i] - x[j])

			SOMA1 = SOMA1 + y[i]*P1
		Y.append(SOMA1)

	# Interpolação para um único ponto xp qualquer
	SOMA2  = 0
	for i in range(N1):
		P2 = 1
		for j in range(N1):
			if(j != i):
				P2 = P2 * (xp - x[j])/(x[i] - x[j])

		SOMA2 = SOMA2 + y[i]*P2

	print("\n O valor da Interpolação no Ponto x = %.3f é  y = %.5f" %(xp,SOMA2))

	# Plotagem dos Gráficos Observado vs Interpolação
	pyplot.title('Gráfico: Observado vs Interpolação')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x,y, label = 'Observado', color = 'blue', linestyle = 'solid')
	pyplot.plot(X,Y, label = 'Interpolação', color = 'red', linestyle = 'dashed')
	pyplot.legend()
	pyplot.grid()
	pyplot.show()
