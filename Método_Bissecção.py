# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:46:18 2019
@author: engoliveira

"""

# Método Numérico da Bissecção

import numpy
import matplotlib.pyplot as pyplot

def g(x):

    return(numpy.exp(-3*x)*numpy.sin(4*x))

def Bissecção(g,x0,x1):
    erro = 0.0000001
    var_count = 1
   
    #Método Numérico da Bissecção
    if(g(x0)*g(x1)<0):
        print("\n")
        print("Iteração\t Ponto(x0)\t Ponto(x1)\t |g(m)|")
        while(abs(x1-x0)>erro):
            m = (x0+x1)/2        
            print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,x0,x1,abs(g(m),)))
            if(abs(x1-x0)<erro or abs(g(m))<erro):
                break
            else:
                if(g(x0)*g(m)>0):
                    x0 = m
                else:
                    x1 = m
            var_count = var_count + 1                    
        print("\n") 
        print("A raiz da função é: %.8f" %(m))    
    else:
        print("\n") 
        print("Não existe raiz nesse intervalo.")

    #Plotagem do Gráfico de G(x)
    xt = numpy.linspace(0.80*m,1.20*m)

    pyplot.title('Gráfico de g(x)')
    pyplot.xlabel('EIXO X')
    pyplot.ylabel('EIXO Y')
    pyplot.plot(xt,g(xt), color = "red")
    pyplot.fill_between(xt,g(xt), color = "gray")
    pyplot.grid()
    pyplot.show()
