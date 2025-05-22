import numpy as np
import matplotlib.pyplot as plt

# ===================== PARTE A =========================

def produto_escalar (mult1, mult2):

    produto = sum(mult1 * mult2)
    return produto

def escalonador (A,b):
    n = len(A)

    for k in range(n-1):
        for i in range (k+1, n):
            aux = A[i][k]
            b[i] = b[i] - b[k] * (aux / A[k][k])
            for j in range (k,n):
                A[i][j] = A[i][j] - A[k][j] * (aux / A[k][k])
    
    return A,b

def substituicao_regressiva (A,b):
    n = len(b)
    x = np.zeros(n)

    for i in reversed(range(n)):
        soma = 0
        for j in range (i+1,n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma)/A[i][i]

    return x

# APROXIMAÇÃO POLINOMIAL DE GRAU 2
def polinomio2grau (x,y):
    n = len(x) # para sabermos quantos elementos tem no vetor x

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
def polinomio3grau (x,y):
    n = len(x) 

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
    n = len(x)

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



# importar os dados da tabela para a variável dados
dados = np.loadtxt('Populacao_PresidentePrudente.dat')
x = dados[:,0]
y = dados[:,1]

w = polinomio2grau(x,y)
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