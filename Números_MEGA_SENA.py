# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:38:09 2020
@author: engoliveira

"""

# Sorteio de Números da Mega Sena

import random
import os

def numeros_mega(h):
	numb = []
	for i in range(h):
		numb.clear()
		while(len(numb)<6):
			X = random.randint(1,60)
			if(X in numb):
				numb.remove(X)
			else:
				numb.append(X)

		numb.sort()

		for j in range(6):
			if(numb[j]<10):
				numb[j] = str("0" + str(numb[j]))
			else:
				numb[j] = str(numb[j])

		print(numb)	

	return(numb)

numeros_mega(int(input("Quantos Sorteios Deseja Realizar? ")))

os.system("pause")