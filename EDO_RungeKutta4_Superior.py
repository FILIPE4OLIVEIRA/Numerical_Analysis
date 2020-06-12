# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""
# EDO: y" + P(x)y' + Q(x)y = R(x)

# Este método resolve o problema da EDO y" - (2/x)y' + (2/x²)y = xln(x) ; y(1) = 1 ; y'(1) = 0

# Método de Runge Kutta 4° Ordem
import numpy
import matplotlib.pyplot as pyplot

# Função
def P(x):
	return(-2/x)

def Q(x):
	return(2/(x**2))

def R(x):
	return(x*numpy.log(x))

# Método de Runge Kutta 4° Ordem
def Runge_Kutta_O4S(x0,x1,y0,y1,P,Q,R):

	numb_div = 100000
	h = (x1-x0)/numb_div

	x_aprox  = [x0]
	y_aprox  = [y0]
	dy_aprox = [y1]

	for i in range(numb_div):

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
	pyplot.title("Solução Numérica da EDO: y'' - (2/x)y' + (2/x²)y = xln(x)\n y(1) = 1 ; y'(1) = 0")
	pyplot.xlabel('EIXO X')
	pyplot.ylabel('EIXO Y')
	pyplot.plot(x_aprox,y_aprox, label = "Solução Númerica y(x)", color = 'blue', linestyle = 'dashed')
	pyplot.plot(x_aprox,dy_aprox, label = "Solução Númerica y'(x)", color = 'green', linestyle = 'dashed')
	pyplot.legend(loc = 'best')
	pyplot.grid(linestyle = '--', linewidth = 0.5)
	pyplot.show()