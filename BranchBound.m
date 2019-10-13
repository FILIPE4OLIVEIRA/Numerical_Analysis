% ================================================================================================
% Algoritmo para solu��o do Problema do "Ponto de Equil�brio de Produ��o" 
% Inicia��o Cient�fica/TCC - UNIVASF 2017.2
% Autor: FILIPE CARDOSO DE OLIVEIRA
% ================================================================================================
function[Z,X] = BranchBound(f,A,b) 
    
    options = optimoptions('linprog','Algorithm','interior-point');     % Inputs de par�metros para fun��o linprog 
    
    [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo m�todo de pontos interiores  
    
    w = x < 0.0001;               % Verifica se o valor na posi��o � menor que uma toler�ncia
    x(w) = 0;                     % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida
    x = x';  
    
    Dados(1) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',0,'s2',0,'expandable',2,'exitFlag',exitFlag);     % Salva os Dados do PL em uma estrutura
    
    [s1] = TesteInteiro(x);         % Fun��o que testa se todos os valores do vetor x s�o inteiros
    if s1 == 1
        fprintf('o PL possui solu��o inteira: %d',x);
    else 
    i=1; s1=0; s2=0; h1=1; h2=1; W1=0;
    Nivel = 0; Noh = i+1;
    R1 = Dados(1).fval;           % Salva o valor Z �timo do PL 
    gap1 = 1;
    tree(Noh/2) = 0;              % Salva a raiz da �rvore para constru��o do gr�fico 
   
        while ( gap1 > 0.05 && W1 == 0 && Noh <= (2^10) )
          
            if ( mod(i,2) ~= 0 )
                
                if (Dados(Noh/2).s1 ~= 1)
                  tree(Noh) = (Noh/2);
                else
                  
                end        
                
                Nivel = fix(log(Noh)/log(2));
                
% ------------- ATUALIZANDO DADOS PARA C�LCULO DO NOVO PL NO N� -------------% 

                A = Dados(Noh/2).A;            % Recupera a matriz do n� acima
                b = Dados(Noh/2).b;            % Recupera o vetor coluna do n� acima
                x = Dados(Noh/2).x;            % Recupera o vetor linha do n� acima   
                
% ------------- AJUSTANDO AS VARI�VEIS DO SUBPROBLEMA -------------%

                w = x < 0.0001;                % Verifica se o valor na posi��o � menor que uma toler�ncia
                x(w) = 0;                      % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida
                
                [s1,k1] = TesteInteiro(x);     % Fun��o que testa se todos os valores do vetor x s�o inteiros 
                
                    if ( s1 == 0 )
                     x(1,k1) = fix(x(1,k1));   % Arredonda para o inteiro inferior o valor de x na posi��o
                     A(end+1,k1) = 1;          % Aumenta em uma linha o tamanho da matriz e atribui um valor a posi��o
                     b(end+1,1) = x(1,k1);     % Aumenta o tamanho do vetor coluna b e atribui um valor a posi��o     
                    else
                    
                    end
% ------------- RESOLVE O NOVO SUBPROBLEMA -------------%   
          
                [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo m�todo de pontos interiores
                 
                    if exitFlag == -2
                        
                       Dados(Noh) = Dados(Noh/2);
                       Dados(Noh).exitFlag = -2;
                       
                    else
                     
                x = x';
                x = round(x*1e5)/1e5;         % Trunca os dados do vetor x para 5 casas decimais 
                
                w = x < 0.0001;               % Verifica se o valor na posi��o � menor que uma toler�ncia
                x(w) = 0;                     % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida
                                  
% ------------- VERIFICANDO SE TODAS AS VARI�VEIS S�O INTEIRAS -------------%   

                [s1] = TesteInteiro(x);        % Fun��o que testa se todos os valores do vetor x s�o inteiros             

% ------------- VERIFICANDO SE TODAS AS RESTRI��ES S�O ATENDIDAS -------------%     
         
                [s2] = TesteRestricoes(A,b,x); % Fun��o que testa se todas as restri��es s�o respeitadas

% ------------- SALVA OS DADOS EM UMA ESTRUTURA -------------%  

                 Dados(Noh) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',s1,'s2',s2,'expandable',0,'exitFlag',exitFlag);
                    
                    end

% ------------- AJUSTA A BANDEIRA DE VERIFICA��O -------------%

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
                
                    
% ------------- ATUALIZANDO DADOS PARA C�LCULO DO NOVO PL NO N� -------------% 

                A = Dados(i/2).A;                  % Recupera a matriz do n� acima
                b = Dados(i/2).b;                  % Recupera o vetor coluna do n� acima
                x = Dados(i/2).x;                  % Recupera o vetor linha do n� acima          
                
% ------------- AJUSTANDO AS VARIAVEIS DO SUBPROBLEMA -------------% 

                w = x < 0.0001;                    % Verifica se o valor na posi��o � menor que uma toler�ncia
                x(w) = 0;                          % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida
                
                [s1,k1] = TesteInteiro(x);         % Fun��o que testa se todos os valores do vetor x s�o inteiros
                    
                    if ( s1 == 0 )
                      x(1,k1) = ceil(x(1,k1));     % Arredonda para o inteiro superior o valor de x na posi��o
                      A(end+1,k1) = -1;            % Aumenta em uma linha o tamanho da matriz e atribui um valor a posi��o
                      b(end+1,1) = -1*x(1,k1);     % Aumenta o tamanho do vetor coluna b e atribui um valor a posi��o
                    else
                    
                    end
% ------------- RESOLVE O NOVO SUBPROBLEMA -------------%   
                  
                [x,fval,exitFlag] = linprog(f,A,b,[],[],[],[],[],options);  % Calcula o PL pelo m�todo de pontos interiores
                                  
                    if exitFlag == -2
                        
                       Dados(Noh) = Dados(i/2);
                       Dados(Noh).exitFlag = -2;
                       
                    else
                    
                x = x';  
                x = round(x*1e5)/1e5;           % Trunca os dados do vetor x para 5 casas decimais 
                
                w = x < 0.0001;                 % verifica se o valor na posi��o � menor que uma toler�ncia
                x(w) = 0;                       % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida 
                                  
% ------------- VERIFICANDO SE TODAS AS VARI�VEIS S�O INTEIRAS -------------% 

                [s1] = TesteInteiro(x);         % Fun��o que testa se todos os valores do vetor x s�o inteiros

% ------------- VERIFICANDO SE TODAS AS RESTRI��ES S�O ATENDIDAS -------------%              

                [s2] = TesteRestricoes(A,b,x);  % Fun��o que testa se todas as restri��es s�o respeitadas

% ------------- SALVA OS DADOS EM UMA ESTRUTURA -------------% 

                 Dados(Noh) = struct('fval',fval,'A',A,'b',b,'x',x,'s1',s1,'s2',s2,'expandable',0,'exitFlag',exitFlag);
                    
                    end
                    
% ------------- AJUSTA A BANDEIRA DE VERIFICA��O -------------%                
                    
                    if ( s1 == 1 || exitFlag == -2)
                      Dados(Noh).expandable = 1; 
                    else
                      Dados(Noh).expandable = 2;      
                    end
                    [W1] = TesteNohs(Noh,Dados);                % Testa os n�s para determinar a parada da �rvore
            end
                if (s1 == 1 && s2 == 1)
                    solutions(h1) = struct('Z',fval,'X',x);     % Salva os dados �timos encontrados em uma estrutura
                    R2 = solutions(h1).Z;                       % Faz R2 igual ao �ltimo dado �timo encontrado
                    gap1 = (abs(R1-R2))/(abs(R1)+1);            % Calcula a diferen�a entre o resultado �timo PL e o resultado �timo PLI
                    h1 = h1+1;                                  % Incrementa a vari�vel para pr�xima posi��o 
                else
                    infactivelsolutions(h2) = struct('Z',fval,'X',x,'A',A,'b',b);   % Salva os dados n�o �timos em um estrutura
                    h2 = h2+1;                                                      % Incrementa a vari�vel para pr�xima posi��o              
                end
                i = i+1;        % Incrementa a vari�vel para pr�xima posi��o
                Noh = i+1;      % Incrementa a vari�vel para pr�xima posi��o
        end
    end
       Z = min([solutions.Z]);              % Localiza o menor valor no campo Z da estrutura
       s3 = find([solutions.Z] == Z);       % Localiza a posi��o de Z na estrutura
       X = solutions(s3).X;                 % Localiza o vetor X associado a posi��o
       treeplot([tree]);                    % Plota a �rvore de busca ao final da execu��o
end
