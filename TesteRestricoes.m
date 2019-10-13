
function [s2] = TesteRestricoes(A,b,x)

% ------------- AJUSTANDO AS VARI�VEIS PARA OS C�CULOS -------------% 

         Afac = A*x';  
         Afac = round(Afac*1e3)/1e3;
         tam2 = size(Afac);                      % Calcula o tamanho do vetor coluna Afac
         u2 = tam2(1,1);                         % Faz u2 igual ao tamanho do vetor coluna Afac
         vetorvec = mod(Afac,1);
         w = vetorvec < 0.0001;                  % Verifica se o valor na posi��o � menor que uma toler�ncia
         vetorvec(w) = 0; 
         
% ------------- VERIFICANDO SE TODAS AS RESTRI��ES S�O ATENDIDAS -------------%   

         k2 = 1;                                 % Inicializa uma contagem
         s2 = 1;                                 % Inicializa uma contagem
         while(s2==1 && k2<=u2)    
               s2 = le(Afac(k2,1),b(k2,1));      % Atribui um valor boleano a vari�vel s2
               k2 = k2+1;                        % Incrementa a vari�vel k2
         end
         return
end