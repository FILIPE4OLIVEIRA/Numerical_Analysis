# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:16:09 2019
@author: engoliveira

"""

# Método Numérico de Newton

import numpy
import matplotlib.pyplot as pyplot

def y(x):

    return(numpy.exp(-3*x)*numpy.sin(4*x))

def dydx(x):
    
    return(numpy.exp(-3*x)*(4*numpy.cos(4*x)-3*numpy.sin(4*x)))
 
def Newton(y,dydx,x0):
    erro = 0.0000001
    maxint = 100
    var_count = 1
    
    #Método Numérico de Newton   
    if(abs(y(x0))<erro):
        print("\n")
        print("A raiz aproximada da função é: %.8f"%(x0))
    else:
        print("Iteração\t Ponto(x1)\t |G(x1)|")
        while(var_count<maxint and abs(y(x0))>erro):
            x1 = x0 - (y(x0)/dydx(x0))
            print("%d\t\t %.8f\t %.8f" %(var_count,x1,abs(y(x1))))
            x0 = x1
            var_count = var_count + 1

        if(var_count>maxint):
            print("\n")
            print("ERRO: Numero Máximo de Iterações Atingido!")
        else:
            print("\n")
            print("A raiz aproximada da função é: %.8f" %(x0))
    
    #Plotagem do Gráfico de G(x)
    xt = numpy.linspace(0.80*x0,1.20*x0)

    pyplot.title('Gráfico de y(x)')
    pyplot.xlabel('EIXO X')
    pyplot.ylabel('EIXO Y')
    pyplot.plot(xt,y(xt), color = "red", label = "y(x) = e^(-3x)sin(4x)")
    pyplot.fill_between(xt,y(xt), color = "gray")
    pyplot.legend(loc = 'best')
    pyplot.grid()
    pyplot.show()
