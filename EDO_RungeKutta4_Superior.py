# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""

# EDO: y" + P(x)y' + Q(x)y = R(x)

# y" - 2y' + 2y = sin(x)e^(2x)

# y(0) = -0.4 ; y'(0) = -0.6

# Método de Runge Kutta 4° Ordem
import numpy
import matplotlib.pyplot as pyplot

# Funções P(x); Q(x); R(x)
def P(x):
    Px = -2
    return(Px)
    
def Q(x):
    Qx = 2
    return(Qx)

def R(x):
    Rx = numpy.exp(2*x)*numpy.sin(x)
    return(Rx)

# Método de Runge Kutta 4° Ordem
def Runge_Kutta_O4S(x0,x1,y0,y1,N=50000):

	h = (x1-x0)/N

	x_aprox  = [x0]
	y_aprox  = [y0]
	dy_aprox = [y1]

	for i in range(N):

		k11 = h*(dy_aprox[i])
		k12 = h*(R(x_aprox[i]) - P(x_aprox[i])*(dy_aprox[i]) - Q(x_aprox[i])*(y_aprox[i]))

		k21 = h*(dy_aprox[i] + (1/2)*k12)
		k22 = h*(R(x_aprox[i] + h/2) - P(x_aprox[i])*(dy_aprox[i] + (1/2)*k12) - Q(x_aprox[i])*(y_aprox[i] + (1/2)*k11))

		k31 = h*(dy_aprox[i] + (1/2)*k22)
		k32 = h*(R(x_aprox[i] + h/2) - P(x_aprox[i])*(dy_aprox[i] + (1/2)*k22) - Q(x_aprox[i])*(y_aprox[i] + (1/2)*k21))

		k41 = h*(dy_aprox[i] + k32)
		k42 = h*(R(x_aprox[i] + h) - P(x_aprox[i])*(dy_aprox[i] + k32) - Q(x_aprox[i])*(y_aprox[i] + k31))

		y_next  = y_aprox[i]  + (1/6)*(k11 + 2*k21 + 2*k31 + k41)
		dy_next = dy_aprox[i] + (1/6)*(k12 + 2*k22 + 2*k32 + k42) 

		y_aprox.append(y_next)
		dy_aprox.append(dy_next)
		x_aprox.append(x_aprox[i] + h)

	print("\n")
	print("A função y(x) no ponto %.2f é aproximadamente: %.8f" %(x1,y_aprox[-1]))


	# Plotagem do Gráfico 1
	pyplot.title("Solução Numérica da EDO:\n y'' - 2y' + 2y = sin(x)e^(2x) \n y(0) = -0.4 ; y'(0) = -0.6")
	pyplot.plot(x_aprox,y_aprox, label = "Solução Númerica y(x)", color = 'blue', linestyle = 'dashed')
	pyplot.plot(x_aprox,dy_aprox, label = "Solução Númerica y'(x)", color = 'green', linestyle = 'dashed')
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()
