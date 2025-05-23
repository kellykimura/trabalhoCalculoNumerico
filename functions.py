import numpy as np
import matplotlib.pyplot as plt

# ===================== PARTE A =========================

def produto_escalar (mult1, mult2):
    """
    Produto escalar de dois vetores vetor.
    
    Parameters
    ----------
    mult1 : float
            valor que está no array.
    
    mult2 : float
            valor que está no outro array.

    Returns 
    -------
    produto : int
            soma das multiplicações
    """

    produto = sum(mult1 * mult2)
    return produto

def escalonador (A,b):
    """
    Eliminação de Gauss.
    
    Parameters
    ----------
    A : array
        Matriz.
    
    b : float
        vetor independente do sistema escalar.

    Returns 
    -------
    A : array
        retorna a matriz escalonada.

    b : array
        vetor do sistema independente.
    """
    n = len(A)

    for k in range(n-1):
        for i in range (k+1, n):
            aux = A[i][k]
            b[i] = b[i] - b[k] * (aux / A[k][k])
            for j in range (k,n):
                A[i][j] = A[i][j] - A[k][j] * (aux / A[k][k])
    
    return A,b

def substituicao_regressiva (A,b):
    """
    Sistema linear triangular superior para solução de matrizes

    Parameters
    ----------
    A : array
        matriz triangular superior 
    b : array
        vetor dos termos independentes

    Returns
    -------
    x : array
        vetor solução 
    """
    n = len(b)
    x = np.zeros(n)

    for i in reversed(range(n)):
        soma = 0
        for j in range (i+1,n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma)/A[i][i]

    return x

# APROXIMAÇÃO POLINOMIAL DE GRAU 2
def polinomio_grau_2 (x,y):
    """
    Mínimos quadrados de polinômio de grau 2 do tipo
    P(x) = w_0 + w_1*x + w_2*x**2

    Parameters
    ----------
    x : int
        vetor dos valores dependentes
    y : int
        vetor dos valores independentes
    Returns
    -------
    w : array 
        coeficientes do polinômio ajustado
    """

    e0 = x**0 # cria um vetor de n números 1's 
    e1 = x**1
    e2 = x**2 # pega o vetor x e multiplica cada elemento ao quadrado

    lista = [e0, e1, e2]

    A = np.zeros((3,3)) # cria uma matriz 3x3

    for i in range(3):
        for j in range(3):
            A[i][j] = produto_escalar(lista[i], lista[j])

    # agora a gente faz as multiplicações escalares, combinando a base com y
    b = np.zeros(3)
    for i in range(3):
        b[i] = produto_escalar(lista[i], y)
    
    print(f"A: {A}")
    print(f"\n\nb: {b}")

    # resolver o sistema com eliminação de gauss
    A,b = escalonador(A,b)
    w = substituicao_regressiva(A,b)

    print(f"A: {A}")
    print(f"\n\nb: {b}")

    return w

# APROXIMAÇÃO POLINOMIAL DE GRAU 3
def polinomio_grau_3 (x,y):
    """
    Mínimos quadrados de polinômio de grau 3 do tipo
    P(x) = w_0 + w_1*x + w_2*x**2 + w_3*x**3

    Parameters
    ----------
    x : int
        vetor dos valores independentes
    y : int
        vetor dos valores dependentes
    Returns
    -------
    w : array 
        coeficientes do polinômio ajustado
    """

    e0 = x**0
    e1 = x**1
    e2 = x**2
    e3 = x**3

    lista = [e0, e1, e2, e3]

    A = np.zeros((4,4))

    for i in range(4):
        for j in range(4):
            A[i][j] = produto_escalar(lista[i], lista[j])

    # multiplicações escalares combinando com y
    b = np.zeros(4)
    for i in range(4):
        b[i] = produto_escalar(lista[i], y)

    # resolver sistema
    A,b = escalonador(A,b)
    w = substituicao_regressiva(A,b)

    return w

# APROXIMAÇÃO POR FUNÇÃO EXPONENCIAL
def exponencial (x,y):
    """
    Modelo de crescimento exponencial do tipo
    y = a * exp(b*x)

    Parameters
    ----------
    x : array
        vetor com os valores da variável independente

    y : array
        vetor com os valores da variável dependente
    
    Returns
    -------
    a : float 
        Coeficiente multiplicativo da função exponencial
    b : float 
        Expoente linear

    """

    e0 = x**0
    e1 = x**1
    lny = np.log(y)

    lista = [e0,e1]
    A = np.zeros((2,2))

    for i in range(2):
        for j in range(2):
            A[i][j] = produto_escalar(lista[i],lista[j])
    
    # multiplicação de y
    b = np.zeros(2)
    for i in range(2):
        b[i] = produto_escalar(lista[i], lny)
    
    # resolver o sistema
    A,b = escalonador(A,b)
    w = substituicao_regressiva(A,b)

    a = np.exp(w[0]) # ln(a)
    b = w[1]

    return a,b

# APROXIMAÇÃO POR FUNÇÃO GEOMÉTRICA


# APROXIMAÇÃO POR FUNÇÃO HIPERBÓLICA
def hiperbólica(x, y):
    """
    Ajuste de uma função hiperbólica do tipo 
    y = a / (x+b) => 1/y = b/a + (1/a)x

    Parameters
    ----------
    x : array
        vetor com os valores da variável independente

    y : array
        vetor com os valores da variável dependente
    
    Returns
    -------
    a : float 
        Coeficiente od numerador da função hiperbólica (escala do decaimento)
    b : float 
        Termo somado ao denominador (desloca a curva no eixo x)
    """
    inv_y = 1 / y
    e0, e1 = x**0, x**1
    # montar mínimos quadrados
    A = np.array([
        [produto_escalar(e0, e0), produto_escalar(e0, e1)],
        [produto_escalar(e1, e0), produto_escalar(e1, e1)]
    ])
    b = np.array([produto_escalar(e0, inv_y), produto_escalar(e1, inv_y)])

    A_aux, b_aux = A, b

    A, b = escalonador(A_aux, b_aux)
    coef = substituicao_regressiva(A, b)
    a = 1 / coef[1]
    b = coef[0] * a
    return a, b

# CALCULAR VALORES DE Y AJUSTADOS
# Y DO POLINÔMIO DE GRAU 2
def ajustado_grau2 (x,y):
    w = polinomio_grau_2(x,y)
    return w[0] + w[1]*x + w[2]*x*2

# Y DO POLINÔMIO DE GRAU 3
def ajustado_grau3 (x,y):
    w = polinomio_grau_3(x,y)
    return w[0] + w[1]*x + w[2]*x2 + w[3]*x*3

# Y DA FUNÇÃO EXPONENCIAL 
def ajustado_exponencial (x,y):
    #  y = a * exp(bx)
    a,b = exponencial(x,y)
    return a * np.exp(b * x)

# Y DA FUNÇÃO GEOMÉTRICA
# y = a * b^x => ln(y) = ln(a) + x * ln(b)

# Y DA FUNÇÃO HIPERBÓLICA
#  y = a / (b + x)




# importar os dados da tabela para a variável dados
dados = np.loadtxt('Populacao_PresidentePrudente.dat')
x = dados[:,0]
y = dados[:,1]

w = polinomio_grau_2(x,y)
print(f"\n\nW: {w}")

plt.scatter(x, y, label='Dados reais')
plt.xlabel('Ano (A)')
plt.ylabel('População (P)')
plt.title('Gráfico de População Presidente Prudente')
plt.grid(True)

# Curva ajustada
x_ajuste = np.linspace(min(x), max(x), 200)
y_ajuste = w[0] + w[1]*x_ajuste + w[2]*x_ajuste**2
plt.plot(x_ajuste, y_ajuste, color='red', label='Ajuste Polinomial (grau 2)')
plt.legend()

plt.show()