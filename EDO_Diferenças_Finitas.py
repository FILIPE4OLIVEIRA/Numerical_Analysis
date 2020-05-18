# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:24:18 2020
@author: engoliveira

"""

# Método das Diferenças Finitas - EDO

"""
Este método calcula a EDO  y" - 8x³y' + 4sin(x)y = 50cos(x)  para as condições de contorno y(1) = 1 ; y(2) = 1

y" - 8x³y' + 4sin(x)y = 50cos(x)

y(1) = 1 ; y(2) = 1

"""
import math
import numpy
import matplotlib.pyplot as pyplot

# Funções P(x); Q(x); R(x)
def P(x):
    Px = -(8*x**3)
    return(Px)
    
def Q(x):
    Qx = (4*math.sin(x))
    return(Qx)

def R(x):
    Rx = (50*math.cos(x))
    return(Rx)

# Método das Diferenças Finitas para EDO de Ordem Superior
def Diferenças_Finitas(x0,x1,P,Q,R,y0,y1):

    N = 100             # Espaço de X
    h = (x1-x0)/(N)     # Passo da Função

    x = numpy.linspace(x0,x1,N)
    A = numpy.zeros((N,N))
    B = numpy.zeros(N)

    # Matriz Tridiagonal
    for i in range(N):
        for j in range(N):
            if (i == j):
                A[i][j] = 2 + (h**2)*Q(x[i])

    for i in range(N):
        for j in range(N):
            if(i == j and i>=1):
                A[i][j-1] = -1 - (h/2)*P(x[i])
                A[i-1][j] = -1 + (h/2)*P(x[i-1])

    for i in range(N):
        B[i] = -(h**2)*R(x[i])

    B[000] = -(h**2)*R(x[i]) + (1+(h/2)*P(x[i]))*y0
    B[N-1] = -(h**2)*R(x[i]) + (1+(h/2)*P(x[i]))*y1

    # Gauss_Sidel Method (Solução do Sistema Linear Tridiagonal)
    vec_aprox = numpy.zeros(N)
    erro = [1]*N
    solution = []
    var_count = 0
    max_int = 100

    while(var_count < max_int or numpy.mean(erro) > 0.0001):
        for i in range(N):
            SOMA1 = 0
            for j in range(N):
                if(i != j):
                    SOMA1 = SOMA1 + A[i,j]*vec_aprox[j]
            vec_aprox[i] = (B[i] - SOMA1)/A[i,i]


        for k in range(N):
            SOMA2 = 0
            for h in range(N):
                SOMA2 = SOMA2 + A[k,h]*vec_aprox[h]
                erro[k] = abs(SOMA2 - B[k])

        var_count = var_count + 1

    solution = list(vec_aprox)

    solution.insert(0,y0) # Ajuste do Ponto Inicial
    solution.append(y1)   # Ajuste do Ponto Final

    X = numpy.linspace(x0,x1,len(solution))

    # Gráfico da EDO
    pyplot.title("Gráfico da EDO \n y'' - 8x³y' + 4sin(x)y = 50cos(x); y(1) = 1 ; y(2) = 1")
    pyplot.xlabel('EIXO X')
    pyplot.ylabel('EIXO Y')
    pyplot.plot(X,solution, label = 'Solução Númerica', color = 'red', linestyle = 'dashed')
    pyplot.legend(loc = 'upper left')
    pyplot.grid()
    pyplot.show()
