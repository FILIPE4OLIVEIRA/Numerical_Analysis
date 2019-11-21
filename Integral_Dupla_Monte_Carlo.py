# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:22:38 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def g(x,y):

	return(numpy.exp(x*y)*numpy.sin(x*y))

def integral_dupla(g,x0,x1,y0,y1):
	random_results = []
	random_approximation = []
	random_numb = 1000
	var_count = 0

	while(var_count<10000):
		SOMA1 = 0
		for i in range(random_numb):
			X = x0+(x1-x0)*numpy.random.uniform(0,1,1)
			Y = y0+(y1-y0)*numpy.random.uniform(0,1,1)
			SOMA1 += g(X,Y)
		
		random_approximation = float((x1-x0)*(y1-y0)*(SOMA1/random_numb))
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))

	#Plotagem do Gráfico de G(x,y)
	x = numpy.linspace(x0,x1)
	y = numpy.linspace(y0,y1)
	x,y = numpy.meshgrid(x,y)

	z = g(x,y)
    
    	#Plotagem do Gráfico 1
	figura1 = plt.figure(1)    
	graph1 = Axes3D(figura1)
	graph1.plot_surface(x, y, z, rstride=3, cstride=3, cmap=cm.viridis)
	plt.title('Gráfico de G(x,y)')
	graph1.set_xlabel('EIXO X')
	graph1.set_ylabel('EIXO Y')
	graph1.set_zlabel('EIXO Z')

	#Plotagem do Gráfico 2
	figura2 = plt.figure(2)
	graph2 = figura2.add_subplot(111)
	graph2.contourf(x,y,z,cmap=cm.viridis)
	figura2.colorbar(graph2.contourf(x,y,z,cmap=cm.viridis))
	plt.title('Gráfico de G(x,y)')
	graph2.set_xlabel('EIXO X')
	graph2.set_ylabel('EIXO Y')

	#Plotagem do Gráfico 3
	figura3 = plt.figure(3)
	plt.title('Distribuição da Integral')
	plt.hist(random_results, bins = 30, ec = 'black')
	plt.xlabel('Valor da Integral')
	plt.ylabel('Frequência')

	plt.show()


	#printe do resultado aproximado da função
	print("\n")
	return(print("\tA Integral Aproximada da Função é:%.8f" %(Integral)))
