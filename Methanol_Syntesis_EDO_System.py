# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:16:09 2019
@author: engoliveira

"""

# Sintese de Metanol


import numpy
import matplotlib.pyplot as pyplot
from scipy.integrate import odeint


# Condições Iniciais
CCo_e = 48.77;
CH2_e = 999.83;
CCo2_e = 36.58;
CH2O_e = 0;
CCH3OH_e = 0;
#-------------------------------------------------
R_Linha = 8.31E-05;       # bar m³/ mol Kelvin
F = 3.21E-06;             # m³/s
V = 3.015E-05;            # m³
T = 493.2;                # Kelvin
mcat = 0.0348;            # Kg
#-------------------------------------------------
k1   = (1.07)*numpy.exp(36696.0/(8.3145*T));
k2   = (1.22E+10)*numpy.exp(-94765.0/(8.3145*T));
kwh  = (3453.38)*numpy.exp(0/(8.3145*T));
kH2  = (0.499)*numpy.exp(17197.0/(8.3145*T));   
kH2O = (6.62E-11)*numpy.exp(124119.0/(8.3145*T));
k1eq = (2.39E-13)*numpy.exp(98388.0/(8.3145*T));
k3eq = (2.554E-11)*numpy.exp(58705.0/(8.3145*T));
#-------------------------------------------------
time_simulation = numpy.arange(0,100,0.01)
init_condition  = CCo_e,CH2_e,CCo2_e,CH2O_e,CCH3OH_e
EDO_constantes  = (R_Linha,F,V,T,mcat,k1,k2,kwh,kH2,kH2O,k1eq,k3eq)

def Methanol_Synthesis(y,time_simulation):

    global R_Linha,F,V,T,mcat,k1,k2,kwh,kH2,kH2O,k1eq,k3eq
    
    Co, H2, Co2, H2O, CH3OH = y
    
    parcial_Co = Co*R_Linha*T;
    parcial_H2 = H2*R_Linha*T;
    parcial_Co2 = Co2*R_Linha*T;
    parcial_H2O = H2O*R_Linha*T;
    parcial_CH3OH = CH3OH*R_Linha*T;
    
    r_CH3OH = ((k1*parcial_Co2*parcial_H2)*(1 - (parcial_CH3OH*parcial_H2O)/(k1eq*parcial_Co2*(parcial_H2**3)))/(1 + kwh*(parcial_H2O/parcial_H2) + numpy.sqrt(kH2*parcial_H2) + kH2O*parcial_H2O)**3);                           
 
    r_RWGS =  (k2*parcial_Co2*(1 - k3eq*(parcial_H2O*parcial_Co/parcial_Co2*parcial_H2))/(1 + kwh*(parcial_H2O/parcial_H2) + numpy.sqrt(kH2*parcial_H2) + kH2O*parcial_H2O));

    dCodt    = (F/V)*(CCo_e - Co) - (mcat/V)*r_RWGS;
    dH2dt    = (F/V)*(CH2_e - H2) + (mcat/V)*(r_RWGS - 3*r_CH3OH);
    dCo2dt   = (F/V)*(CCo2_e - Co2) + (mcat/V)*(r_RWGS - r_CH3OH);
    dH2Odt   = (F/V)*(CH2O_e - H2O) + (mcat/V)*(r_CH3OH - r_RWGS );
    dCH3OHdt = (F/V)*(CCH3OH_e - CH3OH) + (mcat/V)*r_CH3OH;
    
    return(dCodt,dH2dt,dCo2dt,dH2Odt,dCH3OHdt)

Methanol_Model = odeint(Methanol_Synthesis, init_condition, time_simulation)
Co,H2,Co2,H2O,CH3OH = Methanol_Model.T

concentration_Co    = (Co/sum(Co))*100
concentration_H2    = (H2/sum(H2))*100
concentration_Co2   = (Co2/sum(Co2))*100
concentration_H2O   = (H2O/sum(H2O))*100
concentration_CH3OH = (CH3OH/sum(CH3OH))*100

pyplot.figure(figsize=(10,5))
pyplot.rcParams['xtick.labelsize'] = 12
pyplot.rcParams['ytick.labelsize'] = 12
pyplot.title("Modelo de Sintese de Metanol", fontsize = 16)
pyplot.xlabel("Tempo de Simulação (segundos)", fontsize = 14)
pyplot.ylabel("Concentração dos Compostos", fontsize = 14)
pyplot.plot(time_simulation, concentration_Co,    'c', lw=1.25, label='Concentração de Co')
pyplot.plot(time_simulation, concentration_H2,    'k', lw=1.25, label='Concentração de H2')
pyplot.plot(time_simulation, concentration_Co2,   'g', lw=1.25, label='Concentração de Co2')
pyplot.plot(time_simulation, concentration_H2O,   'b', lw=1.25, label='Concentração de H2O')
pyplot.plot(time_simulation, concentration_CH3OH, 'r', lw=1.25, label='Concentração de CH3OH')
pyplot.legend(loc = 'best', fontsize =  'x-large')
pyplot.grid(linestyle = '--')
pyplot.show()