# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:24:18 2020
@author: engoliveira

"""

# Método das Diferenças Finitas - EDO

"""
Este método calcula a EDO y" - xy' - y = 2x² para as condições de contorno y(0) = y(1) = 1

y" - xy' - y = 2x²

y(0) = y(1) = 1

"""

import numpy
import matplotlib.pyplot as plt

# Funções
def g(x,dx):
    return(4*(x**2)*(dx**2))
    
def diff1(x,dx):
    return(2 - x*dx)

def diff2(x,dx):
    return(2*(dx**2)-4)

def diff3(x,dx):
    return(2 + x*dx)


def diff(x0,x1,diff1,diff2,diff3,g):

    N = 10
    dx = (x1-x0)/N 

    x = numpy.linspace(x0,x1,N)
    A = numpy.zeros((N,N))
    b = numpy.zeros(N)

    # elementos da diagonal da matriz
    for i in range(N):
        for j in range(N):
            if (i == j):
                A[i][j] = diff2(x[i],dx)

    # elementos fora da diagonal da matriz ()
    for i in range(N):
        for j in range(N):
            if(i == j and i>=1):
                A[i][j-1] = diff1(x[i],dx)
                A[i-1][j] = diff3(x[i],dx)

    for i in range(N):
        b[i] = g(x[i],dx)

    b[000] = g(x[000],dx) - diff1(x[000],dx)
    b[N-1] = g(x[N-1],dx) - diff3(x[N-1],dx)


    # Gauss_Sidel Method
    vec_aprox = numpy.zeros(N)
    erro = [1]*N
    solution = []
    var_count = 0
    max_int = 100

    while(var_count < max_int):
        for i in range(0,N):
            SOMA1 = 0
            for j in range(0,N):
                if(i != j):
                    SOMA1 = SOMA1 + A[i,j]*vec_aprox[j]
            vec_aprox[i] = (b[i] - SOMA1)/A[i,i]


        for k in range(0,N):
            SOMA2 = 0
            for h in range(0,N):
                SOMA2 = SOMA2 + A[k,h]*vec_aprox[h]
                erro[k] = abs(SOMA2 - b[k])
                if(numpy.mean(erro) < 0.00001):
                    var_count = max_int

        var_count = var_count + 1

    solution = list(vec_aprox)

    plt.title('Gráfico da EDO')
    plt.xlabel('EIXO X')
    plt.ylabel('EIXO Y')
    plt.plot(x, solution)
    plt.grid()
    plt.show()