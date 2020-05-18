# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:46:37 2019
@author: engoliveira

"""

# Método Numérico da Secante

import numpy
import matplotlib.pyplot as pyplot

def y(x):

	return(numpy.exp(-3*x)*numpy.sin(4*x))

def Secante(y,x0,x1):
	erro = 0.0000001
	maxint = 100
	var_count = 1

	#Método Numérico da Secante
	if(y(x0)*y(x1)<0):
		x2 = (x0+x1)/2
		print("\n")
		print("Iteração\t Ponto(x0)\t Ponto(x1)\t |g(x2)|")
		while(var_count<maxint and abs(y(x2))>erro):
			x2 = x1 - ((y(x1)*(x1-x0))/(y(x1)-y(x0)))
			print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,x0,x1,abs(y(x2))))
			x0 = x1
			x1 = x2
			var_count = var_count + 1
		
		if(var_count>maxint):
			print("\n")
			print("ERRO: Numero Máximo de Iterações Atingido!")
		else:
			print("\n")
			print("A raiz aproximada da função é: %.8f" %(x2))

	else:
		print("\n")
		print("Não existe raiz nesse intervalo.")

	#Plotagem do Gráfico de G(x)
	xt = numpy.linspace(0.80*x2,1.20*x2)

	pyplot.title('Gráfico de y(x)')
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(xt,y(xt), color = "red", label = "y(x) = e^(-3x)sin(4x)")
	pyplot.fill_between(xt,y(xt), color = "gray")
	pyplot.legend(loc = 'best')
	pyplot.grid()
	pyplot.show()
