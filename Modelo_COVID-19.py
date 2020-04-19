# -*- coding: utf-8 -*-
"""
Created on Abril Jan 06 21:27:18 2020
@author: engoliveira

"""

import numpy
import pandas
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

from datetime import date
from fbprophet import Prophet
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data_covid19 = pandas.read_excel("C:\\Users\\engoliveira\\PYTHON\\DADOS_COVID19.xlsx", sheet_name = 'sheet1')

data_covid19.head()

datas_cases  = list(data_covid19["DATAS_CASES"])
datas_mortes = list(data_covid19["DATAS_MORTES"].dropna())
infec = list(data_covid19["INFECTADOS"])
death = list(data_covid19["MORTES"].dropna())

time_dados_cases  = numpy.ceil(numpy.linspace(0,len(datas_cases),len(datas_cases)))
time_dados_mortes = numpy.ceil(numpy.linspace(0,len(datas_mortes),len(datas_mortes)))
infec_dados = numpy.array(infec).astype(int)
death_dados = numpy.array(death).astype(int)

## MODELO 1 -------------------------------------------------------------------------------------------------------

def model_cases1(x,c1,c2):
    return(c1*numpy.exp(c2*x))

popt,pcov = curve_fit(model_cases1,time_dados_cases,infec_dados,p0 = [0.5,0.5])
c1,c2 = popt
print(popt)

def model_mortes1(x,m1,m2):
    return(m1*numpy.exp(m2*x))

popt,pcov = curve_fit(model_mortes1,time_dados_mortes,death_dados,p0 = [0.5,0.5])
m1,m2 = popt
print(popt)

est_cases1 = model_cases1(len(datas_cases)+1,c1,c2)
print("Estimativa do Modelo de Casos:", round(est_cases1))

est_mortes1 = model_mortes1(len(datas_mortes)+1,m1,m2)
print("Estimativa do Modelo de Mortes:", round(est_mortes1))

infec_cases1 = []
for i in range(len(time_dados_cases)):
    I1 = model_cases1(time_dados_cases[i],c1,c2)
    infec_cases1.append(I1)

infec_cases1.append(est_cases1)

death_cases1 = []
for i in range(len(time_dados_mortes)):
    I2 = model_mortes1(time_dados_mortes[i],m1,m2)
    death_cases1.append(I2)

death_cases1.append(est_mortes1)

time_data_cases  = data_covid19["DATAS_CASES"]
time_data_mortes = data_covid19["DATAS_MORTES"].dropna()

time_data_cases  = time_data_cases.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);
time_data_mortes = time_data_mortes.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

new_time_data_cases    = list(time_data_cases[0])
new_time_data_mortes   = list(time_data_mortes[0])
new_infec_dados = list(infec_dados)
new_death_dados = list(death_dados)

new_infec_dados.append(est_cases1.astype(int))
new_death_dados.append(est_mortes1.astype(int))


# Plotagem do Gráfico Modelo 1 --------------------------------------------------------------------------------------

pyplot.figure(figsize=(16,8))
pyplot.subplot(2,1,1)
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
pyplot.xlim=[datas_cases[0],datas_cases[-1]]
pyplot.ylim(0,est_cases1+5000)

pyplot.plot(data_covid19["DATAS_CASES"],data_covid19["INFECTADOS"],
         marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
pyplot.plot(time_data_cases,infec_cases1, 
            marker = 'H', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format_cases = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format_cases)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

aux1 = 1
for a,b in zip(new_time_data_cases,new_infec_dados):
    if(aux1%2 != 0):
        pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
    aux1 = aux1 + 1

pyplot.legend(loc = 'upper left')
pyplot.grid()

# ----------------------------------------------------------------------------------------------------------------- 

pyplot.figure(figsize=(16,8))
pyplot.subplot(2,1,2)
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Mortos por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Mortes Confirmadas", fontsize = 14)
pyplot.xlim=[datas_mortes[0],datas_mortes[-1]]
pyplot.ylim(0,est_mortes1+750)

pyplot.plot(data_covid19["DATAS_MORTES"],data_covid19["MORTES"],
         marker = 'H', label = "Número de Mortes Confirmadas", color = "blue", linestyle = 'solid')
pyplot.plot(time_data_mortes,death_cases1, 
            marker = 'H', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format_mortes = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format_mortes)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

aux2 = 1
for c,d in zip(new_time_data_mortes,new_death_dados):
    if(aux2%3 != 0):
        pyplot.text(c, d, str(d), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
    aux2 = aux2 + 1

pyplot.legend(loc = 'upper left')
pyplot.grid()

# -----------------------------------------------------------------------------------------------------------------
pyplot.show()

################################################## - SEPARADOR - ##################################################

## MODELO 2 -------------------------------------------------------------------------------------------------------

def model_cases2(x,c1,c2,c3):
    return(c1*numpy.exp(-c2*numpy.exp(-c3*x)))

popt,pcov = curve_fit(model_cases2,time_dados_cases,infec_dados,p0 = [0.5,0.5,0.5])
c1,c2,c3 = popt
print(popt)

def model_mortes2(x,m1,m2,m3):
    return(m1*numpy.exp(-m2*numpy.exp(-m3*x)))

popt,pcov = curve_fit(model_mortes2,time_dados_mortes,death_dados,p0 = [0.5,0.5,0.5])
m1,m2,m3 = popt
print(popt)

est_cases2 = model_cases2(len(datas_cases)+1,c1,c2,c3)
print("Estimativa do Modelo de Casos:", round(est_cases2))

est_mortes2 = model_mortes2(len(datas_mortes)+1,m1,m2,m3)
print("Estimativa do Modelo de Mortes:", round(est_mortes2))

infec_cases2 = []
for i in range(len(time_dados_cases)):
    I1 = model_cases2(time_dados_cases[i],c1,c2,c3)
    infec_cases2.append(I1)

infec_cases2.append(est_cases2)

death_cases2 = []
for i in range(len(time_dados_mortes)):
    I2 = model_mortes2(time_dados_mortes[i],m1,m2,m3)
    death_cases2.append(I2)

death_cases2.append(est_mortes2)

time_data_cases  = data_covid19["DATAS_CASES"]
time_data_mortes = data_covid19["DATAS_MORTES"].dropna()

time_data_cases  = time_data_cases.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);
time_data_mortes = time_data_mortes.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

new_time_data_cases    = list(time_data_cases[0])
new_time_data_mortes   = list(time_data_mortes[0])
new_infec_dados = list(infec_dados)
new_death_dados = list(death_dados)

new_infec_dados.append(est_cases2.astype(int))
new_death_dados.append(est_mortes2.astype(int))


# Plotagem do Gráfico Modelo 2 --------------------------------------------------------------------------------------

pyplot.figure(figsize=(16,8))
pyplot.subplot(2,1,1)
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
pyplot.xlim=[datas_cases[0],datas_cases[-1]]
pyplot.ylim(0,est_cases1+3000)

pyplot.plot(data_covid19["DATAS_CASES"],data_covid19["INFECTADOS"],
         marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
pyplot.plot(time_data_cases,infec_cases2, 
            marker = 'H', label = "Modelo de Ajuste (Curva de Gompertz)", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format_cases2 = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format_cases2)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

aux1 = 1
for a,b in zip(new_time_data_cases,new_infec_dados):
    if(aux1%2 != 0):
        pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
    aux1 = aux1 + 1

pyplot.legend(loc = 'upper left')
pyplot.grid()

# ----------------------------------------------------------------------------------------------------------------- 

pyplot.figure(figsize=(16,8))
pyplot.subplot(2,1,2)
pyplot.rcParams['xtick.labelsize'] = 14
pyplot.rcParams['ytick.labelsize'] = 14

pyplot.title("Brasil: Número de Mortos por COVID-19.",fontsize = 18)
#pyplot.xlabel("Datas de Referência", fontsize = 14)
pyplot.ylabel("Número de Mortes Confirmadas", fontsize = 14)
pyplot.xlim=[datas_mortes[0],datas_mortes[-1]]
pyplot.ylim(0,est_mortes1+750)

pyplot.plot(data_covid19["DATAS_MORTES"],data_covid19["MORTES"],
         marker = 'H', label = "Número de Mortes Confirmadas", color = "blue", linestyle = 'solid')
pyplot.plot(time_data_mortes,death_cases2, 
            marker = 'H', label = "Modelo de Ajuste (Curva de Gompertz)", color = "red", linestyle = 'dashed')

pyplot.gcf().autofmt_xdate()
date_format_mortes2 = mdates.DateFormatter("%d-%b")
pyplot.gca().xaxis.set_major_formatter(date_format_mortes2)
pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

aux2 = 1
for c,d in zip(new_time_data_mortes,new_death_dados):
    if(aux2%3 != 0):
        pyplot.text(c, d, str(d), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
    aux2 = aux2 + 1

pyplot.legend(loc = 'upper left')
pyplot.grid()

# -----------------------------------------------------------------------------------------------------------------
pyplot.show()

################################################## - SEPARADOR - ##################################################

# CALCULOS DAS MÉTRICAS DOS MODELOS -------------------------------------------------------------------------------

del(infec_cases1[-1])
del(infec_cases2[-1])
del(death_cases1[-1])
del(death_cases2[-1])

rmse_cases1  = mean_squared_error(infec_dados, infec_cases1, squared=False)
rmse_cases2  = mean_squared_error(infec_dados, infec_cases2, squared=False)
rmse_mortes1 = mean_squared_error(death_dados, death_cases1, squared=False)
rmse_mortes2 = mean_squared_error(death_dados, death_cases2, squared=False)

print("RMSE_C1 = %.3f\nRMSE_C2 = %.3f" %(rmse_cases1,rmse_cases2))
print("RMSE_M1 = %.3f\nRMSE_M2 = %.3f" %(rmse_mortes1,rmse_mortes2))

rC1 = r2_score(infec_dados, infec_cases1)
rC2 = r2_score(infec_dados, infec_cases2)
rM1 = r2_score(death_dados, death_cases1)
rM2 = r2_score(death_dados, death_cases2)

print("R²_C1 = %.4f\nR²_C2 = %.4f" %(rC1,rC2))
print("R²_M1 = %.4f\nR²_M2 = %.4f" %(rM1,rM2))
