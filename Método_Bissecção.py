# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:46:18 2019
@author: engoliveira

"""

# Método Numérico da Bissecção

import math

erro = 0.0000001
var_count = 1

def function(x):

    return(math.exp(-3*x)*math.sin(4*x))

def intervalo():
    limites = []
    print("digite o intervalo de busca [x0,x1]:")
    for x in range(0,2):
        if(x == 0):
            y = float(input("digite o limite esquerdo x0: "))
            limites.append(y)
        else:
            y = float(input("digite o limite direito x1: "))
            limites.append(y)
    
    return(limites)

I = intervalo()

print("\n")
if(function(I[0])*function(I[1])<0):
    print("Iteração\t Ponto (x0)\t Ponto (x1)\t f(m)")
    while(abs(I[1]-I[0])>erro):

        m = (I[0]+I[1])/2
        
        print("%d\t\t %.8f\t %.8f\t %.8f" %(var_count,I[0],I[1],abs(function(m),)))
        if(abs(I[1]-I[0])<erro or abs(function(m))<erro):
            break
        else:
            if(function(I[0])*function(m)>0):
                I[0] = m
            else:
                I[1] = m
        var_count = var_count + 1                    
    print("\n") 
    print("A raiz da função é: %.8f" %(m))    
else:
    print("\n") 
    print("Não existe raiz nesse intervalo.")