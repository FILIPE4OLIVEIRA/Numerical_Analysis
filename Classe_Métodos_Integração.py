# -*- coding: utf-8 -*-
"""
Created on Tue Fev 10 00:31:15 2020
@author: engoliveira

"""

# Métodos Numéricos para Solução de Integrais

import numpy
import matplotlib.pyplot as pyplot

class Integração():

    def __init__(self,x0_inicial = -3,x1_final = 3,função_inicial = '1/2 + x*numpy.exp(-x**2)'):
        self.x0_inicial     = x0_inicial
        self.x1_final       = x1_final
        self.função         = lambda x: eval(função_inicial)
        self.função_label   = str(função_inicial)

    def Regra_Trapezio(self):
        numb_breaks = 100000
        SOMA1 = 0
        step = (self.x1_final - self.x0_inicial) / numb_breaks

        for x in range(1, numb_breaks):

            SOMA1 += 2 * self.função(self.x0_inicial + x * step)

        Integral = float((step / 2) * (self.função(self.x0_inicial) + SOMA1 + self.função(self.x1_final)))

        # Plotagem do Gráfico de G(x)
        x = numpy.linspace(self.x0_inicial,self.x1_final)

        pyplot.title('Gráfico de g(x)')
        pyplot.xlabel('EIXO X')
        pyplot.ylabel('EIXO Y')
        pyplot.plot(x, self.função(x), color = "red", label = self.função_label)
        pyplot.fill_between(x, self.função(x), color = "gray")
        pyplot.text(x = self.x1_final*0.30, y = self.x1_final*0.10, s = "Área Aproximada = %.8f" %(Integral))
        pyplot.legend(loc = 'upper left')
        pyplot.grid()
        pyplot.show()

        print("\n")
        return(print("\tA Integral Aproximada da Função é: %.8f" % (Integral)))

    def Regra_Simpson(self):
        numb_breaks = 100000
        SOMA1 = 0
        SOMA2 = 0
        step = (self.x1_final - self.x0_inicial) / numb_breaks

        for x in range(1,int((numb_breaks/2)-1)):

            SOMA1 += 2 * self.função(self.x0_inicial + 2 * x * step)

        for x in range(1,int((numb_breaks/2))):

            SOMA2 += 4 * self.função(self.x0_inicial + 2 * (x-1) * step)

        Integral = float((step / 3) * (self.função(self.x0_inicial) + SOMA1 + SOMA2 + self.função(self.x1_final)))

    
        #Plotagem do Gráfico de G(x)
        x = numpy.linspace(self.x0_inicial,self.x1_final)

        pyplot.title('Gráfico de g(x)')
        pyplot.xlabel('EIXO X')
        pyplot.ylabel('EIXO Y')
        pyplot.plot(x, self.função(x), color = "red", label = self.função_label)
        pyplot.fill_between(x, self.função(x), color = "gray")
        pyplot.text(x = self.x1_final*0.30, y = self.x1_final*0.10, s = "Área Aproximada = %.8f" %(Integral))
        pyplot.legend(loc = 'upper left')
        pyplot.grid()
        pyplot.show()
    
        print("\n")
        return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))


    def Regra_Intervalo(self):
        numb_breaks = 100000
        SOMA1 = 0
        step = (self.x1_final - self.x0_inicial) / numb_breaks

        for x in range(0,int((numb_breaks/2))):

            SOMA1 += self.função(self.x0_inicial + 2 * (x+1) * step)

        Integral = float(2 * step * SOMA1)

    
        #Plotagem do Gráfico de G(x)
        x = numpy.linspace(self.x0_inicial,self.x1_final)

        pyplot.title('Gráfico de g(x)')
        pyplot.xlabel('EIXO X')
        pyplot.ylabel('EIXO Y')
        pyplot.plot(x, self.função(x), color = "red", label = self.função_label)
        pyplot.fill_between(x, self.função(x), color = "gray")
        pyplot.text(x = self.x1_final*0.30, y = self.x1_final*0.10, s = "Área Aproximada = %.8f" %(Integral))
        pyplot.legend(loc = 'upper left')
        pyplot.grid()
        pyplot.show()

        print("\n")
        return(print("\tA Integral Aproximada da Função é: %.8f" %(Integral)))
