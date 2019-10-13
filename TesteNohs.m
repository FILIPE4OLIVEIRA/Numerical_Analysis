function [W1] = TesteNohs(Noh,Dados)
       c1 = 1;
       vetorvec = zeros(1,(Noh+1)/2);     % Cria um vetor de zeros do tamanho dos nós que serão avaliados
       for j = (Noh+1)/2:1:Noh            % Verifica a bandeira do vetor do extremo esquerdo até o extremo direito          
           if Dados(j).expandable == 1    % Acessa o valor da bandeira na estrutura na posição j
              vetorvec(1,c1) = 0;
           else
              vetorvec(1,c1) = 1; 
           end
           c1 = c1+1;                     % Incrementa a variável
       end
       vetorvec(vetorvec == 0) = [];      % Retira todos os zeros do vetor
       W1 = isempty(vetorvec);            % Verifica se o vetor é um vetor vazio
end