# Trabalho de cálculo númerico 


O objetivo do trabalho é utilizar o _método dos mínimos quadrados_ sobre uma base de dados da população de Presidente Prudente ao longo dos últimos 80 anos para realizar aproximações, verificar sua qualidade, realizar testes de alinhamento e prever a população também em alguns anos.

## Proposta do trabalho
1. Determinar aproximações pelos métodos dos mínimos quadrados usando funções polinomias (grau 2 e 3), exponencial, hiperbólica e geométrica. 
    1. plotar os gráficos
2. Determinar quais as opções do item (1) melhor se adequa aos dados usando um **teste de alinhamento das aproximações**. Ele é usado para verificação da função escolhida na representação dos dados e é feito a partir da equação
    $$R^2=1-\sum^n_{i=0}\frac{(y_i-\^y_i)^2}{(y_i-\overline{y})^2}$$

    Legenda da equação
    - $n$: dimensão do vetor
    - $y$: dados coletados
    - $\overline{y}$: média aritmética dos valores de y
    - $\^{y}$: vetor aproximação calculado pelo método dos mínimos quadrados
    

    Resultados de $R^2$
    - $R^2 \approx 0$: bom
    - $R^2 \approx 1$: próximos (aceitável)
    - $R^2 < 0$: péssimo
        - Nesse caso, aproximação por $\overline{y}$ é melhor que os métodos dos mínimos quadrados  

3. Utilizando a função que melhor se adequa aos dados, estimar a população para o ano de 2030 

    

## Pacotes utilizados

> pandas
> matplotlib
> numpy


## Colaboradores 
[Matheus de Almeida Virissimo](https://github.com/matheusvirissimo)

[Kelly Akari Kimura](https://github.com/kellykimura) 