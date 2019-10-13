% ================================================================================================
% Algoritmo para solução do Problema do "Ponto de Equilíbrio de Produção" 
% Iniciação Científica/TCC - UNIVASF 2017.2
% Autor: FILIPE CARDOSO DE OLIVEIRA
% ================================================================================================
function[Z,X] = BranchBound(f,A,b) 
    
    options = optimoptions('linprog','Algorithm','interior-point');     % Inputs de parâmetros para função linprog 
    
    [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo método de pontos interiores  
    
    w = x < 0.0001;               % Verifica se o valor na posição é menor que uma tolerância
    x(w) = 0;                     % Atribui valor zero a esse valor na pocição caso seja menor que a tolerância definida
    x = x';  
    
    Dados(1) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',0,'s2',0,'expandable',2,'exitFlag',exitFlag);     % Salva os Dados do PL em uma estrutura
    
    [s1] = TesteInteiro(x);         % Função que testa se todos os valores do vetor x são inteiros
    if s1 == 1
        fprintf('o PL possui solução inteira: %d',x);
    else 
    i=1; s1=0; s2=0; h1=1; h2=1; W1=0;
    Nivel = 0; Noh = i+1;
    R1 = Dados(1).fval;           % Salva o valor Z ótimo do PL 
    gap1 = 1;
    tree(Noh/2) = 0;              % Salva a raiz da árvore para construção do gráfico 
   
        while ( gap1 > 0.05 && W1 == 0 && Noh <= (2^10) )
          
            if ( mod(i,2) ~= 0 )
                
                if (Dados(Noh/2).s1 ~= 1)
                  tree(Noh) = (Noh/2);
                else
                  
                end        
                
                Nivel = fix(log(Noh)/log(2));
                
% ------------- ATUALIZANDO DADOS PARA CÁLCULO DO NOVO PL NO NÓ -------------% 

                A = Dados(Noh/2).A;            % Recupera a matriz do nó acima
                b = Dados(Noh/2).b;            % Recupera o vetor coluna do nó acima
                x = Dados(Noh/2).x;            % Recupera o vetor linha do nó acima   
                
% ------------- AJUSTANDO AS VARIÁVEIS DO SUBPROBLEMA -------------%

                w = x < 0.0001;                % Verifica se o valor na posição é menor que uma tolerância
                x(w) = 0;                      % Atribui valor zero a esse valor na pocição caso seja menor que a tolerância definida
                
                [s1,k1] = TesteInteiro(x);     % Função que testa se todos os valores do vetor x são inteiros 
                
                    if ( s1 == 0 )
                     x(1,k1) = fix(x(1,k1));   % Arredonda para o inteiro inferior o valor de x na posição
                     A(end+1,k1) = 1;          % Aumenta em uma linha o tamanho da matriz e atribui um valor a posição
                     b(end+1,1) = x(1,k1);     % Aumenta o tamanho do vetor coluna b e atribui um valor a posição     
                    else
                    
                    end
% ------------- RESOLVE O NOVO SUBPROBLEMA -------------%   
          
                [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo método de pontos interiores
                 
                    if exitFlag == -2
                        
                       Dados(Noh) = Dados(Noh/2);
                       Dados(Noh).exitFlag = -2;
                       
                    else
                     
                x = x';
                x = round(x*1e5)/1e5;         % Trunca os dados do vetor x para 5 casas decimais 
                
                w = x < 0.0001;               % Verifica se o valor na posição é menor que uma tolerância
                x(w) = 0;                     % Atribui valor zero a esse valor na pocição caso seja menor que a tolerância definida
                                  
% ------------- VERIFICANDO SE TODAS AS VARIÁVEIS SÃO INTEIRAS -------------%   

                [s1] = TesteInteiro(x);        % Função que testa se todos os valores do vetor x são inteiros             

% ------------- VERIFICANDO SE TODAS AS RESTRIÇÕES SÃO ATENDIDAS -------------%     
         
                [s2] = TesteRestricoes(A,b,x); % Função que testa se todas as restrições são respeitadas

% ------------- SALVA OS DADOS EM UMA ESTRUTURA -------------%  

                 Dados(Noh) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',s1,'s2',s2,'expandable',0,'exitFlag',exitFlag);
                    
                    end

% ------------- AJUSTA A BANDEIRA DE VERIFICAÇÃO -------------%

                    if ( s1 == 1 || exitFlag == -2)
                      Dados(Noh).expandable = 1; 
                    else
                      Dados(Noh).expandable = 2;    % Salva os dados em uma estrutura   
                    end
                
            else
                
                if (Dados(i/2).s1 ~= 1)
                  tree(Noh) = (i/2);
                else
                  
                end
                
                    
% ------------- ATUALIZANDO DADOS PARA CÁLCULO DO NOVO PL NO NÓ -------------% 

                A = Dados(i/2).A;                  % Recupera a matriz do nó acima
                b = Dados(i/2).b;                  % Recupera o vetor coluna do nó acima
                x = Dados(i/2).x;                  % Recupera o vetor linha do nó acima          
                
% ------------- AJUSTANDO AS VARIAVEIS DO SUBPROBLEMA -------------% 

                w = x < 0.0001;                    % Verifica se o valor na posição é menor que uma tolerância
                x(w) = 0;                          % Atribui valor zero a esse valor na pocição caso seja menor que a tolerância definida
                
                [s1,k1] = TesteInteiro(x);         % Função que testa se todos os valores do vetor x são inteiros
                    
                    if ( s1 == 0 )
                      x(1,k1) = ceil(x(1,k1));     % Arredonda para o inteiro superior o valor de x na posição
                      A(end+1,k1) = -1;            % Aumenta em uma linha o tamanho da matriz e atribui um valor a posição
                      b(end+1,1) = -1*x(1,k1);     % Aumenta o tamanho do vetor coluna b e atribui um valor a posição
                    else
                    
                    end
% ------------- RESOLVE O NOVO SUBPROBLEMA -------------%   
                  
                [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo método de pontos interiores
                                  
                    if exitFlag == -2
                        
                       Dados(Noh) = Dados(i/2);
                       Dados(Noh).exitFlag = -2;
                       
                    else
                    
                x = x';  
                x = round(x*1e5)/1e5;           % Trunca os dados do vetor x para 5 casas decimais 
                
                w = x < 0.0001;                 % verifica se o valor na posição é menor que uma tolerância
                x(w) = 0;                       % Atribui valor zero a esse valor na pocição caso seja menor que a tolerância definida 
                                  
% ------------- VERIFICANDO SE TODAS AS VARIÁVEIS SÃO INTEIRAS -------------% 

                [s1] = TesteInteiro(x);         % Função que testa se todos os valores do vetor x são inteiros

% ------------- VERIFICANDO SE TODAS AS RESTRIÇÕES SÃO ATENDIDAS -------------%              

                [s2] = TesteRestricoes(A,b,x);  % Função que testa se todas as restrições são respeitadas

% ------------- SALVA OS DADOS EM UMA ESTRUTURA -------------% 

                 Dados(Noh) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',s1,'s2',s2,'expandable',0,'exitFlag',exitFlag);
                    
                    end
                    
% ------------- AJUSTA A BANDEIRA DE VERIFICAÇÃO -------------%                
                    
                    if ( s1 == 1 || exitFlag == -2)
                      Dados(Noh).expandable = 1; 
                    else
                      Dados(Noh).expandable = 2;      
                    end
                    [W1] = TesteNohs(Noh,Dados);                % Testa os nós para determinar a parada da árvore
            end
                if (s1 == 1 && s2 == 1)
                    solutions(h1) = struct('Z',fval,'X',x);     % Salva os dados ótimos encontrados em uma estrutura
                    R2 = solutions(h1).Z;                       % Faz R2 igual ao último dado ótimo encontrado
                    gap1 = (abs(R1-R2))/(abs(R1)+1);            % Calcula a diferença entre o resultado ótimo PL e o resultado ótimo PLI
                    h1 = h1+1;                                  % Incrementa a variável para próxima posição 
                else
                    infactivelsolutions(h2) = struct('Z',fval,'X',x,'A',A,'b',b);   % Salva os dados não ótimos em um estrutura
                    h2 = h2+1;                                                      % Incrementa a variável para próxima posição              
                end
                i = i+1;        % Incrementa a variável para próxima posição
                Noh = i+1;      % Incrementa a variável para próxima posição
        end
    end
       Z = min([solutions.Z]);              % Localiza o menor valor no campo Z da estrutura
       s3 = find([solutions.Z] == Z);       % Localiza a posição de Z na estrutura
       X = solutions(s3).X;                 % Localiza o vetor X associado a posição
       treeplot([tree]);                    % Plota a árvore de busca ao final da execução
end
