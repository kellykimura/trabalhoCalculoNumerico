import numpy as np 

data = np.loadtxt("./data/Populacao_PresidentePrudente.dat")

populacao = data[:,1].astype(int)

def teste_alinhamento_r2(populacao, ajuste_aproximado):
    # R = 1 - R^2=1-\sum^n_{i=0}\frac{(y_i-\^y_i)^2}{(y_i-\overline{y})^2}

    media_populacao = np.mean(populacao) # faz a média aritmética
    # Usando o sum do numpy para evitar qualquer problema
    numerador = np.sum((populacao - ajuste_aproximado) ** 2)
    denominador = np.sum((populacao - media_populacao) ** 2)

    r = 1 - (numerador/denominador)
    return r