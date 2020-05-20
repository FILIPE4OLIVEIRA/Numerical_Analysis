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

    def Metodo_Trapezio(self):
        numb_breaks = 100000000
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

    def Metodo_Simpson(self):
        numb_breaks = 100000000
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

    def Metodo_Intervalo(self):
        numb_breaks = 100000000
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

    def Metodo_MonteCarlo(self):
        random_results = []
        random_numb = 1000
        var_count = 0

        while(var_count<4500):
            SOMA1 = 0
            for x in range(random_numb):
                X = self.x0_inicial+(self.x1_final - self.x0_inicial)*numpy.random.uniform(0,1,1)
                SOMA1 += self.função(X)
            
            random_approximation = float((self.x1_final - self.x0_inicial)*(SOMA1/random_numb))
            random_results.append(random_approximation)
            var_count = var_count + 1


        Integral = float(numpy.mean(random_results))

        #Plotagem do Gráfico de y(x)
        x = numpy.linspace(self.x0_inicial,self.x1_final)

        #Plotagem do Gráfico 1
        pyplot.title('Gráfico de y(x)')
        pyplot.xlabel('EIXO X')
        pyplot.ylabel('EIXO Y')
        pyplot.plot(x,self.função(x), color = "red", label = self.função_label)
        pyplot.fill_between(x,self.função(x), color = "gray")
        pyplot.text(x = -self.x1_final*0.07, y = self.x1_final*0.12, 
                    s = "Área Aproximada = %.8f" %(Integral))
        pyplot.legend(loc = 'upper left')
        pyplot.grid(linestyle = '--', linewidth = 0.5)
        pyplot.show()

        #Plotagem do Gráfico 2
        pyplot.figure(2)
        pyplot.title('Distribuição Normal dos Resultados da Integral')
        pyplot.hist(random_results, bins = 30, ec = 'black')
        pyplot.xlabel('Valor Médio da Integral')
        pyplot.ylabel('Frequência')
        pyplot.grid(linestyle = '--', linewidth = 0.5)
        pyplot.show()
