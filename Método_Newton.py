# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:16:09 2019
@author: engoliveira

"""

# Método Numérico de Newton

import math

erro = 0.0000001
maxint = 100
var_count = 1

def function(x):

    return(math.exp(-3*x)*math.sin(4*x))

def diffunction(x):
    
    return(math.exp(-3*x)*(4*math.cos(4*x)-3*math.sin(4*x)))
    
x0 = float(input("digite o chute inicial x0: "))

print("\n")
if(abs(function(x0))<erro):
	print("A raiz aproximada da função é: %.8f"%(x0))
else:
    print("Iteração\t Ponto (x)\t f(x)")
    while(var_count<maxint and abs(function(x0))>erro):
    	
    	x1 = x0 - (function(x0)/diffunction(x0))

    	print("%d\t\t %.8f\t %.8f" %(var_count,x1,abs(function(x1))))

    	x0 = x1
    	var_count = var_count + 1

    if(var_count>maxint):
    	print("\n")
    	print("ERRO: Numero Máximo de Iterações Atingido!")
    else:
    	print("\n")
    	print("A raiz aproximada da função é: %.8f" %(x0))
