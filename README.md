# Numerical_Analysis
Este é um repositório com métodos numéricos simples para iniciantes em programação Python e Cálculo Numérico.
## Números Primos:
Estee código retorna a lista de números primos até um limite estabelicido pelo usuário.<br> 
Exemplo: Se o usuário deseja saber a lista de números primos até o 100 o código retorna<br>
A lista de numeros primos é:<br>
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

## Métodos para Raizes de Funções de uma variável:
Os métodos a seguir retornam a raiz de uma função g(x) qualquer definida no início do código,
o código neceessita de mais dois argumentos x0 e x1 que definem o intervalo de busca pela raiz.<br><br>

**Exemplo Método da Bissecção:**<br>
Deseja-se saber a raiz da função ![Equação_1](https://latex.codecogs.com/png.latex?g%28x%29%20%3D%20e%5E%7B-3x%7Dsin%284x%29) no intervalo **[0.5,1.0]**.<br>
Executa o código e chama-se a função **bissecção(g,0.5,1.0)** no console.<br>

**RESULTADO BISSECÇÃO**

Iteração |Ponto(x0)    |Ponto(x1)    | Módulo g(m)
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

![Bissecção](https://github.com/FILIPE4OLIVEIRA/Numerical_Analysis/blob/master/Figure_1_graph_g(x).png)<br>
**A raiz da função é: 0.78539801**<br><br>

**Exemplo Método da Secante:**<br>
Deseja-se saber a raiz da função ![Equação_1](https://latex.codecogs.com/png.latex?g%28x%29%20%3D%20e%5E%7B-3x%7Dsin%284x%29) no intervalo **[0.5,1.0]**.<br>
Executa o código e chama-se a função **secante(g,0.5,1.0)** no console.<br>

**RESULTADO SECANTE**

Iteração |Ponto(x0)  |Ponto(x1)  |Módulo g(x2)
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

![Secante](https://github.com/FILIPE4OLIVEIRA/Numerical_Analysis/blob/master/Figure_1_graph_g(x).png)<br>
**A raiz aproximada da função é: 0.78539816**<br><br>

**Exemplo Método de Newton:**<br>
Deseja-se saber a raiz da função ![Equação_1](https://latex.codecogs.com/png.latex?G%28x%29%20%3D%20e%5E%7B-3x%7Dsin%284x%29) com um chute inicial igual a **0.5**<br>
Neste método é necessario adicionar a derivada da função G(x)
Executa o código e chama-se a função **newton(G,g,0.5)** no console.<br>

**RESULTADO NEWTON**

Iteração |Ponto(x1)  |G(x1)
---------|-----------|----------
1        |0.70701233 |0.03698312
2        |0.77221590 |0.00519687
3        |0.78490800 |0.00018611
4        |0.78539744 |0.00000027
5        |0.78539816 |0.00000000

![Secante](https://github.com/FILIPE4OLIVEIRA/Numerical_Analysis/blob/master/Figure_2_graph_g(x).png)<br>
**A raiz aproximada da função é: 0.78539816**<br><br>

## Métodos de Integração para Funções de uma variável:
