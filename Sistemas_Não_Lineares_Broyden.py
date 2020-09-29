# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:44:36 2020
@author: engoliveira

"""

# Método de Broyden para Sistemas Não Lineares
import numpy
from numpy.linalg import inv as inverse


x0 = [0,0,0]

# Funções Não Lineares
def G1(x1,x2,x3):
	return(3*x1 - numpy.cos(x2*x3) - 1/2)

def G2(x1,x2,x3):
	return(x1**2 - 81*((x2 + 0.1)**2) + numpy.sin(x3) + 1.06)

def G3(x1,x2,x3):
	return(numpy.exp(-x1*x2) + 20*x3 + (10*numpy.pi - 3)/3)

# Calculo do Sistema Não Linear
def Non_Linear_System(x0):
    
    F1 = G1(x0[0],x0[1],x0[2])
    F2 = G2(x0[0],x0[1],x0[2])
    F3 = G3(x0[0],x0[1],x0[2])

    System_Value = list((round(i,10) for i in [F1,F2,F3]))
    
    return(System_Value)

# Calculo da Matriz Jacobiana do Sistema Não Linear
def Jacobiano(x0,h=0.001):
    
    x1,x2,x3 = x0[0], x0[1], x0[2]
    
    dG1dx1 = (G1(x1+h,x2,x3) - G1(x1,x2,x3))/h
    dG1dx2 = (G1(x1,x2+h,x3) - G1(x1,x2,x3))/h
    dG1dx3 = (G1(x1,x2,x3+h) - G1(x1,x2,x3))/h
    
    dG2dx1 = (G2(x1+h,x2,x3) - G2(x1,x2,x3))/h
    dG2dx2 = (G2(x1,x2+h,x3) - G2(x1,x2,x3))/h
    dG2dx3 = (G2(x1,x2,x3+h) - G2(x1,x2,x3))/h
    
    dG3dx1 = (G3(x1+h,x2,x3) - G3(x1,x2,x3))/h
    dG3dx2 = (G3(x1,x2+h,x3) - G3(x1,x2,x3))/h
    dG3dx3 = (G3(x1,x2,x3+h) - G3(x1,x2,x3))/h
    
    Matrix = numpy.array([[dG1dx1,dG1dx2,dG1dx3],
                          [dG2dx1,dG2dx2,dG2dx3],
                          [dG3dx1,dG3dx2,dG3dx3]])
    
    return(Matrix)    

# Método de Broyden para Sistemas Não Lineares
def Broyden_Method(x0,h=0.001,max_int=100):
    
    System_Value = Non_Linear_System(x0)
    System_Value = list(abs(i) for i in System_Value)
    erro_alvo = [0.00001,0.00001,0.00001]
    
    var_count = 0
    while(System_Value > erro_alvo and var_count < max_int):

    	F_x0 = numpy.array(Non_Linear_System(x0))
    	A0 = Jacobiano(x0,h)
    	Inv_A0 = inverse(A0) # Inversa da Matriz Jacobiana
    	x1 = x0 - Inv_A0@F_x0
    	F_x1 = numpy.array(Non_Linear_System(x1))
    	y1 = F_x1 - F_x0
    	s1 = x1 - x0
    	c1 = (s1@Inv_A0)@y1
    	Inv_A1 = Inv_A0 + (1/c1)*((s1-Inv_A0@y1)*(s1@Inv_A0))
    	x2 = x1 - Inv_A1@F_x1
    	x0 = x2

    	System_Value = Non_Linear_System(x0)
    	System_Value = list(abs(i) for i in System_Value)
    	var_count = var_count + 1
   
    xn = list(round(i,10) for i in x0)
    
    print("Número de Iterações: %.i" %var_count)
 
    return(print("Solução do Sistema Não Linear: ", xn))
