# Numerical_Analysis
Este é um repositório com métodos numéricos simples para iniciantes em programação Python e Cálculo Numérico.

## Métodos de Interpolação de Dados:

### Exemplo Método de Lagrange:<br>
Deseja-se interpolar os dados contidos no vetores **x** e **y**.<br>
x = [0,20,40,60,80,100]<br>
y = [26.0,48.6,61.6,71.2,74.8,75.2]	<br>
Executa o código e chama-se a função **Lagrange(x,y,xp)** em que o parâmetro xp é um ponto qualquer pertencente ao intervalo x.<br>
Exemplo: **Lagrange(x,y,43.76)**<br>

**RESULTADO INTERPOLAÇÃO DE LAGRANGE**<br>
![Interpolação_Lagrange](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Interpolação_Lagrange_1.png)

### Exemplo Método de Spline Cúbico:<br>
Deseja-se interpolar os dados contidos no vetores **x** e **y**.<br>
x = [0.125,0.375,0.625,0.875,1.125,1.375,1.625]<br>
y = [0.264,0.840,1.361,1.612,1.366,0.716,0.079]<br>
Executa o código e chama-se a função **Spline_Cubico(x,y,xp)** em que o parâmetro xp é um ponto qualquer pertencente ao intervalo x.<br>
Exemplo: **Spline_Cubico(x,y,0.957)**<br>

**RESULTADO INTERPOLAÇÃO POR SPLINE CUBICO**<br>
![Interpolação_Spline_Cubico](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Interpolação_Spline_Cubico_1.png)

## Métodos para Raizes de Funções de uma variável:
Os métodos a seguir retornam a raiz de uma função y(x) qualquer definida no início do código,
o código necessita de mais dois argumentos x0 e x1 que definem o intervalo de busca pela raiz.<br>

### Exemplo Método da Bissecção:<br>
Deseja-se saber a raiz da função **y(x) = e^(-3x)sin(4x)** no intervalo **[0.5,1.0]**.<br>
Executa o código e chama-se a função **Bissecção(g,0.5,1.0)** no console.<br>

**RESULTADO BISSECÇÃO**

Iteração |Ponto(x0)    |Ponto(x1)    | Módulo y(m)
:-------:|:-----------:|:-----------:|----------
1        |0.50000000   |1.00000000   |0.01487394
2        |0.75000000   |1.00000000   |0.02541065
3        |0.75000000   |0.87500000   |0.00945399
4        |0.75000000   |0.81250000   |0.00159228
5        |0.78125000   |0.81250000   |0.00420237
6        |0.78125000   |0.79687500   |0.00137399
7        |0.78125000   |0.78906250   |0.00009178
8        |0.78515625   |0.78906250   |0.00064543
9        |0.78515625   |0.78710938   |0.00027791
10       |0.78515625   |0.78613281   |0.00009333
11       |0.78515625   |0.78564453   |0.00000084
12       |0.78515625   |0.78540039   |0.00004545
13       |0.78527832   |0.78540039   |0.00002230
14       |0.78533936   |0.78540039   |0.00001073
15       |0.78536987   |0.78540039   |0.00000494
16       |0.78538513   |0.78540039   |0.00000205
17       |0.78539276   |0.78540039   |0.00000060
18       |0.78539658   |0.78540039   |0.00000012
19       |0.78539658   |0.78539848   |0.00000024
20       |0.78539753   |0.78539848   |0.00000006

**A raiz da função é: 0.78539801**<br><br>

### Exemplo Método da Secante:<br>
Deseja-se saber a raiz da função **y(x) = e^(-3x)sin(4x)** no intervalo **[0.5,1.0]**<br>
Executa o código e chama-se a função **Secante(g,0.5,1.0)** no console.<br>

**RESULTADO SECANTE**

Iteração |Ponto(x0)  |Ponto(x1)  |Módulo y(x2)
---------|-----------|-----------|------------
1        |0.50000000 |1.00000000 |0.03265448
2        |1.00000000 |0.92168833 |0.28897198
3        |0.92168833 |0.41273669 |0.02441542
4        |0.41273669 |0.87001488 |0.01593241
5        |0.87001488 |0.83438920 |0.00716276
6        |0.83438920 |0.76747859 |0.00106462
7        |0.76747859 |0.78823032 |0.00005566
8        |0.78823032 |0.78554505 |0.00000048
9        |0.78554505 |0.78539691 |0.00000000

**A raiz aproximada da função é: 0.78539816**<br><br>

### Exemplo Método de Newton:<br>
Deseja-se saber a raiz da função **y(x) = e^(-3x)sin(4x)** com um chute inicial igual a **0.5**,
neste método é necessário adicionar a função **y'(x)**<br>
Executa o código e chama-se a função **Newton(y,dydx,0.5)** no console.<br>

**RESULTADO NEWTON**

Iteração |Ponto(x1)  |y(x1)
---------|-----------|----------
1        |0.70701233 |0.03698312
2        |0.77221590 |0.00519687
3        |0.78490800 |0.00018611
4        |0.78539744 |0.00000027
5        |0.78539816 |0.00000000

**A raiz aproximada da função é: 0.78539816**<br><br>

**Resultado Gráfico das Funções Bissecção, Secante e Newton.**
![Zero_Funções](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/graph_zero_g(x).png)<br>

## Métodos de Integração para Funções de uma Variável:
Os métodos a seguir realizam a integração de uma função g(x) em um intervalo [x0,x1] qualquer.<br>

### Exemplo Método do (1/2) Trapezio Composto:<br>
Deseja-se saber o valor da integral **∫(1/2+xe^(-x^2)dx** no itervalo **[-2,2]**<br>
Executa o código e chama-se a função **Trapezio(g,-2,2)** no console.<br>

**RESULTADO TRAPEZIO**<br>
![Trapezio](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Area_Function_Trapezio.png)<br>
**A Integral Aproximada da Função é: 2.00000000**<br><br>

### Exemplo Método do (1/3) Simpson Composto:<br>
Deseja-se saber o valor da integral **∫(1/2+xe^(-x^2)dx** no itervalo **[-2,2]**<br>
Executa o código e chama-se a função **Simpson(g,-2,2)** no console.<br>

**RESULTADO SIMPSON**<br>
![Simpson](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Area_Function_Simpson.png)<br>
**A Integral Aproximada da Função é: 1.99550328**<br><br>

### Exemplo Método do Ponto Médio:<br>
Deseja-se saber o valor da integral **∫(1/2+xe^(-x^2)dx** no itervalo **[-2,2]**<br>
Executa o código e chama-se a função **Ponto_Medio(g,-2,2)** no console.<br>

**RESULTADO PONTO MÉDIO**<br>
![Ponto_Médio](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Area_Function_Ponto_Medio.png)<br>
**A Integral Aproximada da Função é: 2.00029305**<br><br>

## Método Estocástico de Integração para Funções com Multiplas Variáveis:
A seguir utiliza-se o método de Monte Carlo para realizar a Integração de funções com uma ou mais variáveis.

### Exemplo Integral Simples:<br>
Deseja-se calcular a Integral **∫(1/2+xe^(-x^2)dx** no itervalo **[-2,2]**<br>
Executa o código e chama-se a função **Integral_Simples(g,-2,2)**<br> 
Por padrão serão sorteados 1000 números aleatórios e 15000 simulações.<br>

**RESULTADO INTEGRAL ESTOCÁSTICA SIMPLES**<br>
![Integral_Simples_1](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Area_Function_MonteCarlo.png)<br>
![Integral_Simples_2](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Distribuição_Integral_Simples.png)<br>
**A Integral Aproximada da Função é: 2.00577996**<br><br>

### Exemplo Integral Dupla:<br>
Deseja-se calcular a Integral **∬e(^xy)sin⁡(xy)dxdy** sobre a região **β = [x0,x1,y0,y1]**<br>
Executa o código e chama-se a função **Integral_Dupla(g,0,1,0,1)**<br> 
Por padrão serão sorteados 1000 números aleatórios e 15000 simulações.<br>

**RESULTADO INTEGRAL ESTOCÁSTICA DUPLA**<br>
![Integral_Dupla_1](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_1_Dupla.png)<br>
![Integral_Dupla_2](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_2_Dupla.png)<br>
![Integral_Dupla_3](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_3_Dupla.png)<br>
**A Integral Aproximada da Função é: 0.38769407**<br><br>

### Exemplo Integral Tripla:<br>
Deseja-se calcular a Integral da função **∭sin⁡(xyz)dxdydz** **β = [x0,x1,y0,y1,z0,z1]**<br>
Executa o código e chama-se a função **Integral_Tripla(g,-2,2,-2,2,-0.2,0.3)**<br> 
Por padrão serão sorteados 1000 números aleatórios e 15000 simulações.<br>

**RESULTADO INTEGRAL ESTOCÁSTICA TRIPLA**<br>
![Integral_Tripla_1](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_1_Tripla.png)<br>
![Integral_Tripla_2](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_2_Tripla.png)<br>
![Integral_Tripla_2](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/Figure_3_Tripla.png)<br>
**A Integral Aproximada da Função é: -0.00137981**<br><br>

## Métodos Númericos para Solução de EDOs

### Exemplo Método de Euler: <br>
Este método resolve o problema da EDO y' - 2xy = 0 ; y(1) = 1  no intervalo **x = [0,2]**<br>
Executa o código e chama-se a função **Euler_Method(g,0,2,1)**<br>

**RESULTADO MÉTODO DE EULER**<br>
![EDO_Euler](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/EDO_Euler.png)<br>

### Exemplo Método de Runge Kutta 4° Ordem: <br>
Este método resolve o problema da EDO y' - 2xy = 0 ; y(1) = 1  no intervalo **x = [0,2]**<br>
Executa o código e chama-se a função **Runge_Kutta_O4(g,0,2,1)**<br>

**RESULTADO MÉTODO DE RUNGE KUTTA 4° ORDEM**
![EDO_RK4](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/EDO_RK4.png)<br>

### Exemplo Método de Diferenças Finitas: <br>
Este método calcula a EDO  y" - 8x³y' + 4sin(x)y = 50cos(x)  para as condições de contorno y(1) = 1 ; y(2) = 1<br>
Executa o código e chama-se a função **Diferenças_Finitas(1,2,P,Q,R,1,1)**<br>

**RESULTADO MÉTODO DE DIFERENÇAS FINITAS**
![EDO_Diferenças Finitas](https://github.com/FILIPE4OLIVEIRA/FILIPE4REPOSITORY/blob/master/Imagens/EDO_Diferenças_Finitas.png)<br>
