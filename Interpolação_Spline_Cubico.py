# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 06:00:09 2020
@author: engoliveira

"""

# Este método interpola os dados apresentados no vetores x e y a partir de splines cubicos
# Também é possível calcular o valor da interpolação em um ponto usando a variável xp.

# Interpolação Spline Cubico

import numpy
import matplotlib.pyplot as pyplot

x = [0.125,0.375,0.625,0.875,1.125,1.375,1.625]    	# DADOS EIXO X
y = [0.264,0.840,1.361,1.612,1.366,0.716,0.079]		# DADOS EIXO Y

def Spline_Cubico(x,y,xp):

	N1 = len(x)
	
	Hx = []
	Hy = []

	A = numpy.zeros((N1,N1))
	B = numpy.zeros(N1)

	for i in range(0,N1-1):
		XX = (x[i+1] - x[i])
		Hx.append(XX)

	for i in range(0,N1-1):
		YY = (y[i+1] - y[i])
		Hy.append(YY)

	# Elementos da Diagonal
	for i in range(N1):
		for j in range(N1):
			if (i == j and i>0):
				A[i][j] = 2*(Hx[i-2] + Hx[i-1])

	A[0][0] = A[N1-1][N1-1] = 1

	# Elementos Superior e Inferior
	for i in range(N1-1):
		for j in range(N1-1):
			if(i == j and i>=1):
				A[i][j-1] = Hx[i-2]
				A[i][j+1] = Hx[i-1]

	# Elemntos do Vetor B
	for i in range(N1-1):
		B[i] = (3/Hx[i])*(y[i+1] - y[i]) - (3/Hx[i-1])*(y[i] - y[i-1])

	B[00] = B[N1-1] = 0

	# Gauss_Sidel Method (Solução do Sistema Linear Associado)
	vec_aprox = numpy.zeros(N1)
	erro = [1]*(N1)
	solution = []
	var_count = 0
	max_int = 100

	while(var_count < max_int):
		for i in range(N1):
			SOMA1 = 0
			for j in range(N1):
				if(i != j):
					SOMA1 = SOMA1 + A[i,j]*vec_aprox[j]
				vec_aprox[i] = (B[i] - SOMA1)/A[i,i]


		for n in range(N1):
			SOMA2 = 0
			for p in range(N1):
				SOMA2 = SOMA2 + A[n,p]*vec_aprox[p]
				erro[n] = abs(SOMA2 - B[n])
				if(numpy.mean(erro) < 0.00001):
					var_count = max_int

		var_count = var_count + 1

	C = vec_aprox

	beta = [0]*(N1-1)
	delta = [0]*(N1-1)


	# Cálculo do Parâmetros das Funções Parciais
	for i in range(N1-1):
		beta[i] = (Hy[i]/Hx[i]) - (Hx[i]/3)*(C[i+1] + 2*C[i])
		delta[i] = (C[i+1] - C[i])/(3*Hx[i])

	# Interpolação para um Ponto xp
	for i in range(N1-1):
		if(xp>=x[i] and xp<=x[i+1]):
			SOMA3 = y[i] + beta[i]*(xp-x[i]) + C[i]*((xp-x[i])**2) + delta[i]*((xp-x[i])**3)

	print("\n O valor da Interpolação no Ponto x = %.3f é  y = %.5f" %(xp,SOMA3))

	# Interpolação para Todos os Pontos
	Intervalo = []
	for i in range(N1-1):
		K = numpy.linspace(x[i],x[i+1],10000)
		for j in range(len(K)):
			SOMA4 = y[i] + beta[i]*(K[j]-x[i]) + C[i]*((K[j]-x[i])**2) + delta[i]*((K[j]-x[i])**3)	
			Intervalo.append(SOMA4)
	
	X = numpy.linspace(x[0],x[-1],len(Intervalo))
	Y = Intervalo
	
	# Plotagem dos Gráficos Observado vs Interpolação
	pyplot.title('Gráfico: Observado vs Interpolação')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x,y, label = 'Observado', color = 'blue', linestyle = 'solid')
	pyplot.plot(X,Y, label = 'Interpolação', color = 'red', linestyle = 'dashed')
	pyplot.legend()
	pyplot.grid()
	pyplot.show()
