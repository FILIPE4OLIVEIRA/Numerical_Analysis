# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:14:09 2019
@author: engoliveira

"""

# Regra do Ponto Médio

import math

def g(x):

	return(math.exp(-3*x)*math.sin(4*x))

def ponto_médio(g,x0,x1):
	numb_breaks = 1000
	SOMA1 = 0
	step = (x1-x0)/numb_breaks

	for x in range(0,int((numb_breaks/2))):

		SOMA1 += g(x0 + 2*(x+1)*step)

	Integral = float(2*step*SOMA1)

	print("\n")
	return(print("\tA Integral Aproximada da Função é:%.8f" %(Integral)))
