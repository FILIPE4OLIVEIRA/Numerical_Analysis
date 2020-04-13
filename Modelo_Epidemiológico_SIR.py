# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:27:18 2020
@author: engoliveira

"""

import numpy
import matplotlib.pyplot as pyplot
from scipy.integrate import odeint

## Condições Iniciais
N = 1e6
I0 = 1
R0 = 0
S0 = N - I0 - R0

delta  = 0.378   # Coeficiente de Transmissão
gamma  = 1/50    # Taxa de Recuperação
sigma  = 1/250   # Taxa de Novos Suscetíveis

time_days = numpy.linspace(0,180,180) # 180 dias

# Sistema de EDO's
def model_SIR(y,time_days,N,delta,gamma,sigma):
    S, I, R = y
    dSdt = sigma*(N-S) - (delta/N)*I*S
    dIdt = (delta/N)*I*S - I*(sigma + gamma)
    dRdt = gamma*I - sigma*R
    return(dSdt, dIdt, dRdt)

y0 = S0, I0, R0

result = odeint(model_SIR, y0, time_days, args=(N, delta, gamma, sigma))
S, I, R = result.T

# Plotagem do Gráfico
pyplot.figure(figsize=(16,6))
pyplot.rcParams['xtick.labelsize'] = 12
pyplot.rcParams['ytick.labelsize'] = 12
pyplot.title("Modelo Epidemiológico SIR \n ", fontsize = 16)
pyplot.xlabel("Tempo/Dias", fontsize = 14)
pyplot.ylabel("Números de Pessoas", fontsize = 14)
pyplot.plot(time_days, S, 'b', lw=2, label='Saudáveis')
pyplot.plot(time_days, I, 'r', lw=2, label='Infectados')
pyplot.plot(time_days, R, 'g', lw=2, label='Recuperados')
pyplot.text(0.5,545000,r'$\delta$ = 0.378', {'fontsize':15})
pyplot.text(0.5,490000,r'$\gamma$ = 1/50',  {'fontsize':15})
pyplot.text(0.5,425000,r'$\sigma$ = 1/250', {'fontsize':15})
pyplot.legend(loc = 'best', fontsize =  'x-large')
pyplot.grid()
pyplot.show()
