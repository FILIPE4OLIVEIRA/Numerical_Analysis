# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:16:09 2019
@author: engoliveira

"""

# Método Numérico de Newton

import numpy
import matplotlib.pyplot as plt

def G(x):

    return(numpy.exp(-3*x)*numpy.sin(4*x))

def g(x):
    
    return(numpy.exp(-3*x)*(4*numpy.cos(4*x)-3*numpy.sin(4*x)))
 
def newton(G,g,x0):
    erro = 0.0000001
    maxint = 100
    var_count = 1
    
    #Método Numérico de Newton   
    if(abs(G(x0))<erro):
        print("\n")
        print("A raiz aproximada da função é: %.8f"%(x0))
    else:
        print("Iteração\t Ponto(x1)\t |G(x1)|")
        while(var_count<maxint and abs(G(x0))>erro):
            x1 = x0 - (G(x0)/g(x0))
            print("%d\t\t %.8f\t %.8f" %(var_count,x1,abs(G(x1))))
            x0 = x1
            var_count = var_count + 1

        if(var_count>maxint):
            print("\n")
            print("ERRO: Numero Máximo de Iterações Atingido!")
        else:
            print("\n")
            print("A raiz aproximada da função é: %.8f" %(x0))
    
    #Plotagem do Gráfico de G(x)
    x = numpy.linspace(0.95*x0,1.15*x0)

    plt.title('Gráfico de g(x)')
    plt.xlabel('EIXO X')
    plt.ylabel('EIXO Y')
    plt.plot(x,G(x))
    plt.fill_between(x,G(x))
    plt.grid()
    plt.show()
