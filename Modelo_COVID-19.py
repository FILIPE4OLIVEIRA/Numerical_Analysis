# -*- coding: utf-8 -*-
"""
Created on Abril Jan 06 21:27:18 2020
@author: engoliveira

"""

import numpy
import pandas
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
import statsmodels.api as statsmodels

from datetime import date
from fbprophet import Prophet
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data = pandas.read_excel("C:\\Users\\engoliveira\\PYTHON\\DADOS_COVID19.xlsx", sheet_name = 'sheet1')

datas = list(data["DATA"])
infec = list(data["INFECTADOS"])

x_dados = numpy.linspace(0,len(datas),len(datas))
y_dados = numpy.array(infec)


## MODELO 1 ------------------------------------------------------------------------------------

def model_1(x,p1,p2): # Modelo Exponencial Puro
    return(p1*numpy.exp(p2*x))

popt,pcov = curve_fit(model_1,x_dados,y_dados)
p1,p2 = popt
print(popt)

est1 = model_1(len(datas)+1,p1,p2)
print("Estimativa do Modelo:", round(est1))

y_calc1 = []
for i in range(len(x_dados)):
    I = model_1(x_dados[i],p1,p2)
    y_calc1.append(I)

y_calc1.append(est1)

x_data = data["DATA"]
x_data = x_data.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

xdatas = list(x_data[0])
ydados = list(y_dados)
ydados.append(est1.astype(int))

# Plotagem do Gráfico -------------------------------------------------------------------------

pyplot.figure(figsize=(16,8))
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
pyplot.xlim=[datas[0],datas[-1]]

pyplot.plot(data["DATA"],data["INFECTADOS"],
         marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
pyplot.plot(x_data,y_calc1, 
            marker = 'H', label = "Modelo de Ajuste", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

for a,b in zip(xdatas,ydados):
    pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'x-large')

pyplot.legend(loc = 'best')
pyplot.grid()
pyplot.tight_layout()
pyplot.show()


## MODELO 2 ------------------------------------------------------------------------------------

def model_2(x,p1,p2,p3): # Curva de Gompertz
    return(p1*numpy.exp(-p2*numpy.exp(-p3*x)))

popt,pcov = curve_fit(model_2,x_dados,y_dados,p0=[1,0,1])
p1,p2,p3 = popt
print(popt)

est2 = model_2(len(datas)+1,p1,p2,p3)
print("Estimativa do Modelo:", round(est2))

y_calc2 = []
for i in range(len(x_dados)):
    I = model_2(x_dados[i],p1,p2,p3)
    y_calc2.append(I)

y_calc2.append(est2)

x_data = data["DATA"]
x_data = x_data.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

xdatas = list(x_data[0])
ydados = list(y_dados)
ydados.append(est2.astype(int))

# Plotagem do Gráfico -------------------------------------------------------------------------

pyplot.figure(figsize=(16,8))
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
pyplot.xlim=[datas[0],datas[-1]]

pyplot.plot(data["DATA"],data["INFECTADOS"],
         marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
pyplot.plot(x_data,y_calc2, 
            marker = 'H', label = "Modelo de Ajuste", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=3))

for a,b in zip(xdatas,ydados):
    pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'x-large')

pyplot.legend(loc = 'best', fontsize =  'x-large')
pyplot.grid()
pyplot.tight_layout()
pyplot.show()


# Cálculo dos Estimadores de Eficiência RMSE para os 2 modelos ----------------------------------

del(y_calc1[-1])
del(y_calc2[-1])

rmse1 = mean_squared_error(y_dados, y_calc1, squared=False)
rmse2 = mean_squared_error(y_dados, y_calc2, squared=False)

print("RMSE_1 = %.3f\nRMSE_2 = %.3f" %(rmse1,rmse2))

r1 = r2_score(y_dados, y_calc1)
r2 = r2_score(y_dados, y_calc2)

print("R²_1 = %.3f\nR²_2 = %.3f" %(r1,r2))