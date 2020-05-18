# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:38:09 2019
@author: engoliveira

"""

# Lista de Números Primos

import numpy
import matplotlib.pyplot as pyplot
import time

class NumerosPrimos:

    def __init__(self, Numb = 2, list_prime = [2],time = 0):
        self.numb = Numb
        self.list = list_prime
        self.time = time

    def Calcular_Primos(self):

        odd_numb = []       # impares
        even_numb = []      # pares
        self.list  = [2]    # primos

        temp1 = time.time()

        for x in range(2, self.numb + 1):          # Cria um lista de números Pares e Impares
            if (x % 2 == 0):
                even_numb.append(x)
            else:
                odd_numb.append(x)

        for x in range(2, len(odd_numb) + 1):
            for y in range(3, len(odd_numb) + 1):  # Remove todos os múltiplos impares da lista
                z = y * x
                if (z in odd_numb):
                    odd_numb.remove(z)

        for x in odd_numb:                         # Monta o vetor contendo todos os números com resto da divisão igual a zero
            for y in range(3, self.numb + 1):
                if (x % y == 0):
                    self.list.append(x)

        temp2 = time.time()

        self.time = temp2 - temp1

    def Lista_Primos(self):

        P1 = print(" São %.i Números Primos até o Número %.i" % (len(self.list),self.numb))
        P2 = print(" Lista de Números Primos: ", str(self.list))
        print("\n\n")
        P3 = print(" Tempo Total de Execução: %.5f " % self.time)
        print("\n")

        # Plotagem do Gráfico dos Números Primos 
        pyplot.title('Gráfico dos Números Primos')
        pyplot.xlabel('EIXO X')
        pyplot.ylabel('EIXO Y')
        pyplot.plot(self.list, marker = 'H' , label = 'Números Primos', color = 'red', linestyle = 'dotted')
        pyplot.legend(loc = 'best')
        pyplot.grid()
        pyplot.show()

    def Teste_Primos(self):

        print("\n")
        if(self.numb in self.list):
            P4 = print(" O Número %.i é um Número Primo!" % self.numb)
            return(P4)
        else:
            P5 = print(" O Número %.i não é um Número Primo!" % self.numb)
        return(P5)

while(True):
    if(__name__ == '__main__'):
        Numero = NumerosPrimos(int(input("Digite um Número Limite: ")))
        Numero.Calcular_Primos()
        Numero.Teste_Primos()
        Numero.Lista_Primos()
