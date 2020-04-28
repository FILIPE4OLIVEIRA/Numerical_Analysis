# -*- coding: utf-8 -*-
"""
Created on Abril Jan 06 21:27:18 2020
@author: engoliveira

"""

import numpy
import pandas
import statistics
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

from datetime import date
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data_covid19 = pandas.read_excel("C:\\Users\\engoliveira\\PYTHON\\DADOS_COVID19.xlsx", sheet_name = 'sheet1')

data_covid19.head(5)

data_cases  = list(data_covid19["DATAS_CASES"].dropna())
data_mortes = list(data_covid19["DATAS_MORTES"].dropna())
infec = list(data_covid19["INFECTADOS"].dropna())
death = list(data_covid19["MORTES"].dropna())

time_dados_cases  = numpy.ceil(numpy.linspace(0,len(data_cases),len(data_cases)))
time_dados_mortes = numpy.ceil(numpy.linspace(0,len(data_mortes),len(data_mortes)))
infec_dados = numpy.array(infec).astype(int)
death_dados = numpy.array(death).astype(int)

## MODELO 1 ----------------------------------------------------------------------------------------------------------

def model_cases1(x,c1,c2):
    return(c1*numpy.exp(c2*x))

popt,pcov = curve_fit(model_cases1,time_dados_cases,infec_dados, p0 = [0.5,0.5])
c1,c2 = popt
print(popt)

def model_mortes1(x,m1,m2):
    return(m1*numpy.exp(m2*x))

popt,pcov = curve_fit(model_mortes1,time_dados_mortes,death_dados, p0 = [0.5,0.5])
m1,m2 = popt
print(popt)

est_cases1 = model_cases1(len(data_cases)+1,c1,c2)
print("Estimativa do Modelo de Casos (Exponencial Pura):", round(est_cases1))

est_mortes1 = model_mortes1(len(data_mortes)+1,m1,m2)
print("Estimativa do Modelo de Mortes (Exponencial Pura):", round(est_mortes1))

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

time_data_cases1  = data_covid19["DATAS_CASES"]
time_data_mortes1 = data_covid19["DATAS_MORTES"].dropna()

time_data_cases1  = time_data_cases1.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);
time_data_mortes1 = time_data_mortes1.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

new_time_data_cases1    = list(time_data_cases1[0])
new_time_data_mortes1   = list(time_data_mortes1[0])
new_infec_dados1 = list(infec_dados)
new_death_dados1 = list(death_dados)

new_infec_dados1.append(est_cases1.astype(int))
new_death_dados1.append(est_mortes1.astype(int))

## MODELO 2 -----------------------------------------------------------------------------------------------------------

def model_cases2(x,c1,c2,c3):
    return(c1*numpy.exp(-c2*numpy.exp(-c3*x)))

popt,pcov = curve_fit(model_cases2,time_dados_cases,infec_dados, p0 = [0.5,0.5,0.5])
c1,c2,c3 = popt
print(popt)

def model_mortes2(x,m1,m2,m3):
    return(m1*numpy.exp(-m2*numpy.exp(-m3*x)))

popt,pcov = curve_fit(model_mortes2,time_dados_mortes,death_dados, p0 = [1.5,3.5,0.5])
m1,m2,m3 = popt
print(popt)

est_cases2 = model_cases2(len(data_cases)+1,c1,c2,c3)
print("Estimativa do Modelo de Casos (Curva de Gompertz):", round(est_cases2))

est_mortes2 = model_mortes2(len(data_mortes)+1,m1,m2,m3)
print("Estimativa do Modelo de Mortes (Curva de Gompertz):", round(est_mortes2))

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

time_data_cases2  = data_covid19["DATAS_CASES"].dropna()
time_data_mortes2 = data_covid19["DATAS_MORTES"].dropna()

time_data_cases2  = time_data_cases2.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);
time_data_mortes2 = time_data_mortes2.append(pandas.DataFrame([pandas.Timestamp(date.today())]),ignore_index=True);

new_time_data_cases2    = list(time_data_cases2[0])
new_time_data_mortes2   = list(time_data_mortes2[0])
new_infec_dados2 = list(infec_dados)
new_death_dados2 = list(death_dados)

new_infec_dados2.append(est_cases2.astype(int))
new_death_dados2.append(est_mortes2.astype(int))

def statistics_models(x):
    
    adjust_infec_cases1 = infec_cases1.copy()
    adjust_infec_cases2 = infec_cases2.copy()
    adjust_death_cases1 = death_cases1.copy()
    adjust_death_cases2 = death_cases2.copy()
    
    adjust_infec_cases1.remove(adjust_infec_cases1[-1])
    adjust_infec_cases2.remove(adjust_infec_cases2[-1])
    adjust_death_cases1.remove(adjust_death_cases1[-1])
    adjust_death_cases2.remove(adjust_death_cases2[-1])
    
    rmse_cases1  = mean_squared_error(infec_dados, adjust_infec_cases1, squared=False)
    rmse_cases2  = mean_squared_error(infec_dados, adjust_infec_cases2, squared=False)
    rmse_mortes1 = mean_squared_error(death_dados, adjust_death_cases1, squared=False)
    rmse_mortes2 = mean_squared_error(death_dados, adjust_death_cases2, squared=False)

    rC1 = r2_score(infec_dados, adjust_infec_cases1)
    rC2 = r2_score(infec_dados, adjust_infec_cases2)
    rM1 = r2_score(death_dados, adjust_death_cases1)
    rM2 = r2_score(death_dados, adjust_death_cases2)
    
    if(x==1):
        print(" RMSE_C1 = %.3f\tR²_C1 = %.4f\n RMSE_C2 = %.3f\tR²_C2 = %.4f" %(rmse_cases1,rC1,rmse_cases2,rC2))
        print(" RMSE_M1 = %.3f\tR²_M1 = %.4f\n RMSE_M2 = %.3f\tR²_M2 = %.4f" %(rmse_mortes1,rM1,rmse_mortes2,rM2))
    
    rmse_cases = (rmse_cases1,rmse_cases2);
    rmse_morte = (rmse_mortes1,rmse_mortes2);
    
    return(rmse_cases,rmse_morte)

rmse_cases,rmse_morte = statistics_models(0); z_alpha = 1.96/2.0

def prediction_interval():
    uper_cases_model_1 = []; lown_cases_model_1 = []; uper_cases_model_2 = []; lown_cases_model_2 = []
    uper_morte_model_1 = []; lown_morte_model_1 = []; uper_morte_model_2 = []; lown_morte_model_2 = []

    for i in range((len(infec_cases1)-2),len(infec_cases1)):   
        uper_cases_model_1.append(infec_cases1[i] + z_alpha*rmse_cases[0])
        lown_cases_model_1.append(infec_cases1[i] - z_alpha*rmse_cases[0])
        uper_cases_model_2.append(infec_cases2[i] + z_alpha*rmse_cases[1])
        lown_cases_model_2.append(infec_cases2[i] - z_alpha*rmse_cases[1])

    for i in range((len(death_cases1)-2),len(death_cases1)):   
        uper_morte_model_1.append(death_cases1[i] + z_alpha*rmse_morte[0])
        lown_morte_model_1.append(death_cases1[i] - z_alpha*rmse_morte[0])
        uper_morte_model_2.append(death_cases2[i] + z_alpha*rmse_morte[1])
        lown_morte_model_2.append(death_cases2[i] - z_alpha*rmse_morte[1]) 
        
    uper_cases_model_1[0] = infec[-1]
    lown_cases_model_1[0] = infec[-1]
    uper_cases_model_2[0] = infec[-1]
    lown_cases_model_2[0] = infec[-1]

    uper_morte_model_1[0] = death[-1]
    lown_morte_model_1[0] = death[-1]
    uper_morte_model_2[0] = death[-1]
    lown_morte_model_2[0] = death[-1]
    
    interval_cases_model_1 = numpy.ceil((uper_cases_model_1,lown_cases_model_1)).astype(int)
    interval_cases_model_2 = numpy.ceil((uper_cases_model_2,lown_cases_model_2)).astype(int)
    interval_morte_model_1 = numpy.ceil((uper_morte_model_1,lown_morte_model_1)).astype(int)
    interval_morte_model_2 = numpy.ceil((uper_morte_model_2,lown_morte_model_2)).astype(int)
    
    return(interval_cases_model_1,interval_cases_model_2,interval_morte_model_1,interval_morte_model_2)

interval_cases_model_1,interval_cases_model_2,interval_morte_model_1,interval_morte_model_2 = prediction_interval()

# GRÁFICOS  -------------------------------------------------------------------------------------------------------

def graph_model_1():
    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,1)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
    pyplot.xlim=[data_cases[0],data_cases[-1]]
    pyplot.ylim(0,est_cases1+10000)

    pyplot.plot(data_covid19["DATAS_CASES"],data_covid19["INFECTADOS"],
             marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_cases1,infec_cases1, 
                marker = 'H', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')
    pyplot.fill_between(time_data_cases1[0][-2:], interval_cases_model_1[0], interval_cases_model_1[1], 
                        alpha = 0.5, color = "blue")
    pyplot.text(data_covid19["DATAS_CASES"][2],50200,{'Upper Bound':interval_cases_model_1[0][1]}, {'fontsize':15})
    pyplot.text(data_covid19["DATAS_CASES"][2],45000,{'Lower Bound':interval_cases_model_1[1][1]}, {'fontsize':15})

    pyplot.gcf().autofmt_xdate()
    date_format_cases = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_cases)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=3))

    aux1 = 1
    for a,b in zip(new_time_data_cases1,new_infec_dados1):
        if(aux1%2 == 0):
            pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -15)
        aux1 = aux1 + 1

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # ----------------------------------------------------------------------------------------------------------------- 

    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,2)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Mortos por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Mortes Confirmadas", fontsize = 14)
    pyplot.xlim=[data_mortes[0],data_mortes[-1]]
    pyplot.ylim(0,est_mortes1+1750)

    pyplot.plot(data_covid19["DATAS_MORTES"],data_covid19["MORTES"],
             marker = 'H', label = "Número de Mortes Confirmadas", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_mortes1,death_cases1, 
                marker = 'H', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')
    pyplot.fill_between(time_data_mortes1[0][-2:], interval_morte_model_1[0], interval_morte_model_1[1], 
                        alpha = 0.5, color = "blue")
    pyplot.text(data_covid19["DATAS_MORTES"][2],4500,{'Upper Bound':interval_morte_model_1[0][1]}, {'fontsize':15})
    pyplot.text(data_covid19["DATAS_MORTES"][2],4000,{'Lower Bound':interval_morte_model_1[1][1]}, {'fontsize':15})

    pyplot.gcf().autofmt_xdate()
    date_format_mortes = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_mortes)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

    aux2 = 1
    for c,d in zip(new_time_data_mortes1,new_death_dados1):
        if(aux2%2 != 0):
            pyplot.text(c, d, str(d), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
        aux2 = aux2 + 1

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # -----------------------------------------------------------------------------------------------------------------
    pyplot.show()

def graph_model_2():
    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,1)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
    pyplot.xlim=[data_cases[0],data_cases[-1]]
    pyplot.ylim(0,est_cases1+10000)

    pyplot.plot(data_covid19["DATAS_CASES"],data_covid19["INFECTADOS"],
             marker = 'H', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_cases2,infec_cases2, 
                marker = 'H', label = "Modelo de Ajuste (Curva de Gompertz)", color = "red", linestyle = 'dashed')
    pyplot.fill_between(time_data_cases2[0][-2:], interval_cases_model_2[0], interval_cases_model_2[1], 
                        alpha = 0.5, color = "blue")
    pyplot.text(data_covid19["DATAS_CASES"][2],50200,{'Upper Bound':interval_cases_model_2[0][1]}, {'fontsize':15})
    pyplot.text(data_covid19["DATAS_CASES"][2],45000,{'Lower Bound':interval_cases_model_2[1][1]}, {'fontsize':15})

    pyplot.gcf().autofmt_xdate()
    date_format_cases2 = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_cases2)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=3))

    aux1 = 1
    for a,b in zip(new_time_data_cases2,new_infec_dados2):
        if(aux1%2 == 0):
            pyplot.text(a, b, str(b), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
        aux1 = aux1 + 1

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # ----------------------------------------------------------------------------------------------------------------- 

    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,2)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Mortos por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Mortes Confirmadas", fontsize = 14)
    pyplot.xlim=[data_mortes[0],data_mortes[-1]]
    pyplot.ylim(0,est_mortes1+1750)

    pyplot.plot(data_covid19["DATAS_MORTES"],data_covid19["MORTES"],
             marker = 'H', label = "Número de Mortes Confirmadas", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_mortes2,death_cases2, 
                marker = 'H', label = "Modelo de Ajuste (Curva de Gompertz)", color = "red", linestyle = 'dashed')
    pyplot.fill_between(time_data_mortes2[0][-2:], interval_morte_model_2[0], interval_morte_model_1[1], 
                        alpha = 0.5, color = "blue")
    pyplot.text(data_covid19["DATAS_MORTES"][2],4500,{'Upper Bound':interval_morte_model_2[0][1]}, {'fontsize':15})
    pyplot.text(data_covid19["DATAS_MORTES"][2],4000,{'Lower Bound':interval_morte_model_2[1][1]}, {'fontsize':15})
    
    pyplot.gcf().autofmt_xdate()
    date_format_mortes2 = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_mortes2)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

    aux2 = 1
    for c,d in zip(new_time_data_mortes2,new_death_dados2):
        if(aux2%2 != 0):
            pyplot.text(c, d, str(d), ha = 'right', va = 'bottom', fontsize =  'large', rotation = -25)
        aux2 = aux2 + 1

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # -----------------------------------------------------------------------------------------------------------------
    pyplot.show()

def graph_model_3():
    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,1)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Infectados por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Casos Confirmados", fontsize = 14)
    pyplot.xlim=[data_cases[0],data_cases[-1]]
    pyplot.ylim(0,est_cases1+10000)

    pyplot.plot(data_covid19["DATAS_CASES"],data_covid19["INFECTADOS"],
             marker = 'h', label = "Número de Casos Confirmados", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_cases1,infec_cases1, 
                marker = 'h', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')
    pyplot.plot(time_data_cases2,infec_cases2, 
                marker = 'h', label = "Modelo de Ajuste (Curva de Gompertz)", color = "green", linestyle = 'dashed')

    pyplot.gcf().autofmt_xdate()
    date_format_cases2 = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_cases2)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=3))

    pyplot.text(new_time_data_cases1[-1],new_infec_dados1[-1],str(est_cases1.astype(int)), 
                ha = 'right', va = 'bottom', fontsize =  'large', rotation = 0)
    pyplot.text(new_time_data_cases2[-1],new_infec_dados2[-1],str(est_cases2.astype(int)), 
                ha = 'left',  va = 'bottom', fontsize =  'large', rotation = 0)

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # ----------------------------------------------------------------------------------------------------------------- 

    pyplot.figure(figsize=(16,12))
    pyplot.subplot(2,1,2)
    pyplot.rcParams['xtick.labelsize'] = 14
    pyplot.rcParams['ytick.labelsize'] = 14

    pyplot.title("Brasil: Número de Mortos por COVID-19.",fontsize = 18)
    #pyplot.xlabel("Datas de Referência", fontsize = 14)
    pyplot.ylabel("Número de Mortes Confirmadas", fontsize = 14)
    pyplot.xlim=[data_mortes[0],data_mortes[-1]]
    pyplot.ylim(0,est_mortes1+1750)

    pyplot.plot(data_covid19["DATAS_MORTES"],data_covid19["MORTES"],
             marker = 'h', label = "Número de Mortes Confirmadas", color = "blue", linestyle = 'solid')
    pyplot.plot(time_data_mortes1,death_cases1, 
                marker = 'h', label = "Modelo de Ajuste (Exponencial Pura)", color = "red", linestyle = 'dashed')
    pyplot.plot(time_data_mortes2,death_cases2, 
                marker = 'h', label = "Modelo de Ajuste (Curva de Gompertz)", color = "green", linestyle = 'dashed')

    pyplot.gcf().autofmt_xdate()
    date_format_mortes2 = mdates.DateFormatter("%d-%b")
    pyplot.gca().xaxis.set_major_formatter(date_format_mortes2)
    pyplot.gca().xaxis.set_major_locator(mdates.DayLocator(bymonthday=None, interval=2))

    pyplot.text(new_time_data_mortes1[-1],new_death_dados1[-1],str(est_mortes1.astype(int)), 
                ha = 'right', va = 'bottom', fontsize =  'large', rotation = 0)
    pyplot.text(new_time_data_mortes2[-1],new_death_dados2[-1],str(est_mortes2.astype(int)), 
                ha = 'left',  va = 'bottom', fontsize =  'large', rotation = 0)

    pyplot.legend(loc = 'upper left')
    pyplot.grid()

    # -----------------------------------------------------------------------------------------------------------------
    pyplot.show()

def graph_model(number):
    if  (number == 1):
        graph_model_1()
    elif(number == 2):
        graph_model_2()
    else:
        graph_model_3()

graph_model(2)
rmse_cases,rmse_morte = statistics_models(1)
