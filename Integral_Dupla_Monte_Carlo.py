# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:22:38 2019
@author: engoliveira

"""

# Integração de Monte Carlo

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import cm

def g(x,y):

	return(numpy.exp(-3*x*y)*numpy.sin(4*x*y))

def integral_dupla(g,x0,x1,y0,y1):
	random_results = []
	random_numb = 1000
	var_count = 0

	while(var_count<100):
		SOMA1 = 0
		for x in range(random_numb):

			SOMA1 += g(x0+(x1-x0)*numpy.random.uniform(0,1,1),y0+(y1-y0)*numpy.random.uniform(0,1,1))
	
		random_approximation = float((1/random_numb)*SOMA1)
		random_results.append(random_approximation)
		var_count = var_count + 1


	Integral = float(numpy.mean(random_results))

	#Plotagem do Gráfico de G(x,y)
	x = numpy.linspace(x0,x1)
	y = numpy.linspace(y0,y1)
	x,y = numpy.meshgrid(x,y)

	z = g(x,y)
    
	figura1 = plt.figure()    
	graph1 = Axes3D(figura1)
	graph1.plot_surface(x, y, z, rstride=3, cstride=3, cmap=cm.viridis)

	plt.title('Gráfico de g(x,y)')
	graph1.set_xlabel('EIXO X')
	graph1.set_ylabel('EIXO Y')
	graph1.set_zlabel('EIXO Z')

	figura2 = plt.figure()
	graph2 = figura2.add_subplot(111)
	graph2.contourf(x,y,z,cmap=cm.viridis)

	graph2.set_xlabel('EIXO X')
	graph2.set_ylabel('EIXO Y')
	

	plt.grid()
	plt.show()


	#printe do resultado aproximado da função
	print("\n")
	return(print("\tA Integral Aproximada da Função é:%.8f" %(Integral)))