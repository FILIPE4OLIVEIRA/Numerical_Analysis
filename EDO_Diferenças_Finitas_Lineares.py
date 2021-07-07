# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:24:18 2020
@author: engoliveira

"""

# Método das Diferenças Finitas - EDO

"""
EDO: y" + P(x)y' + Q(x)y = R(x)

y" + 2xy' + 3xy = cos(x)

y(0) = 1 ; y(1) = 2

"""
import math
import numpy
import matplotlib.pyplot as pyplot

# Funções P(x); Q(x); R(x)
def P(x):
    Px = -2*x
    return(Px)
    
def Q(x):
    Qx = 3*x
    return(Qx)

def R(x):
    Rx = numpy.cos(x)
    return(Rx)

# Método das Diferenças Finitas para EDO de Ordem Superior

def Diferença_Finita_Linear(x0,y0,x1,y1,N=100):

    dx = (x1-x0)/N

    x = numpy.linspace(x0+dx,x1-dx,N)
    A = numpy.zeros((N,N))
    B = numpy.zeros(N)

    # Matriz Tridiagonal
    for i in range(N):
        for j in range(N):
            if (i == j):
                A[i][j] = 2 + (dx**2)*Q(x[i])
            elif(i == (j+1)):
                A[i][j] = -1 - (dx/2)*P(x[i])
            elif(i == (j-1)):
                A[i][j] = -1 + (dx/2)*P(x[i-1])
            else:
                A[i][j] = 0
    
    # Vetor Solução B 
    for i in range(N):
        if(i == 0):
            B[i] = (1+(dx/2)*P(x[i]))*y0 - R(x[i])*(dx**2)
        elif(i == N-1):
            B[i] = (1 - (dx/2)*P(x[i]))*y1 - R(x[i])*(dx**2)
        else:
            B[i] = -R(x[i])*(dx**2)

    
    # Gauss_Sidel Method (Solução do Sistema Linear Tridiagonal)

    # Critério de Sassenfeld para Convergância 
    def Sassenfeld(A,B):
        coef = list(numpy.ones(len(B)))
        for i in range(len(B)):
            for j in range(len(B)):
                if (i != j):
                    coef[i] = coef[i] + A[i][j]*coef[j]


            coef[i] = coef[i]/A[i][i]

        sf = max(coef)
        
        return(sf)

    # Método de Gauss-Sidel para solução de Sistemas Lineares
    def Gauss_Sidel(A,B,max_int=2000):

        sf = Sassenfeld(A,B)

        vec_aprox = numpy.zeros(N)
        erro = [0.5]*N
        solution = []
        var_count = 0

        while(var_count < max_int and numpy.mean(erro) > 0.0001):
            for i in range(N):
                SOMA1 = 0
                for j in range(N):
                    if(i != j):
                        SOMA1 += A[i,j]*vec_aprox[j]
                vec_aprox[i] = (B[i] - SOMA1)/A[i,i]


            for k in range(N):
                SOMA2 = 0
                for h in range(N):
                    SOMA2 += A[k,h]*vec_aprox[h]
                erro[k] = abs(SOMA2 - B[k]) 
            var_count = var_count + 1

        solution = list(vec_aprox)

        return(solution,var_count,max_int)

    solution,var_count,max_int = Gauss_Sidel(A,B)

    if(var_count<max_int):
        print("\nIterações Necessárias: %.i" %(var_count))
        print("\nAproximação da EDO no Ponto %.1f é de %.8f"%(x1,solution[-1]))
    else:
        print("\nNúmero Máximo de Iterações Antigido: %.i" %(max_int))
        print("\nAproximação da EDO no Ponto %.1f é de %.8f"%(x1,solution[-1]))

    xt = numpy.linspace(x0,x1,len(solution))

    # Gráfico da EDO
    pyplot.title("Gráfico da EDO \n y - 2xy' + 3xy = cos(x); y(0) = 1 ; y(1) = 2")
    pyplot.xlabel('EIXO X')
    pyplot.ylabel('EIXO Y')
    pyplot.plot(xt,solution, label = 'Solução Númerica', color = 'red', linestyle = 'dashed')
    pyplot.legend(loc = 'best')
    pyplot.grid()
    pyplot.show()
