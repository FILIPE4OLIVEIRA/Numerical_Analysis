
function [s1,k1] = TesteInteiro(x)

% ------------- AJUSTANDO AS VARI�VEIS PARA OS C�CULOS -------------% 

        vetorvec = mod(x,1);             % Calcula o modulo do resto da divis�o por 1
        vetorvec = single(vetorvec);     % Singla as variaveis do vetor
        tam1 = size(vetorvec);           % Calcula o tamanho do vetor x
        u1 = tam1(1,2);                  % Faz u1 igual ao tamanho do vetor x  
        w2 = vetorvec < 0.0001;          % Verifica se o valor na posi��o � menor que uma toler�ncia
        vetorvec(w2) = 0;                % Atribui valor zero a esse valor na poci��o caso seja menor que a toler�ncia definida

% ------------- VERIFICANDO SE TODAS AS VARI�VEIS S�O INTEIRAS -------------%  

        i=1;                             % Inicializa uma contagem
        j=1;                             % Inicializa uma contagem
        k1 = 1;                          % Inicializa uma contagem
        s1 = 1;                          % Inicializa uma contagem
        while(s1 == 1 && k1<=u1)  
           s1 = eq(vetorvec(1,k1),0);    % Atribui um valor boleano a vari�vel s1
           k1 = k1+1;                    % Incrementa o valor de k1
        end
        if (vetorvec(1,1) > 0)
            k1 = 1;
        else
            k1 = k1-1;
        end
        return       
end