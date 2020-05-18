# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:46:18 2019
@author: engoliveira

"""

# Método Numérico da Bissecção

import numpy
import matplotlib.pyplot as pyplot

def y(x):

    return(numpy.exp(-3*x)*numpy.sin(4*x))

def Bissecção(y,x0,x1):
    erro = 0.0000001
    var_count = 1
   
    #Método Numérico da Bissecção
    if(y(x0)*y(x1)<0):
        print("\n")
        print("Iteração\t Ponto(x0)\t Ponto(x1)\t |y(m)|")
        while(abs(x1-x0)>erro):
            m = (x0+x1)/2        
            print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,x0,x1,abs(y(m),)))
            if(abs(x1-x0)<erro or abs(y(m))<erro):
                break
            else:
                if(y(x0)*y(m)>0):
                    x0 = m
                else:
                    x1 = m
            var_count = var_count + 1                    
        print("\n") 
        print("A raiz da função é: %.8f" %(m))    
    else:
        print("\n") 
        print("Não existe raiz nesse intervalo.")

    #Plotagem do Gráfico de y(x)
    xt = numpy.linspace(0.80*m,1.20*m)

    pyplot.title('Gráfico de g(x)')
    pyplot.xlabel('EIXO X')
    pyplot.ylabel('EIXO Y')
    pyplot.plot(xt,y(xt), color = "red")
    pyplot.fill_between(xt,y(xt), color = "gray")
    pyplot.grid()
    pyplot.show()
