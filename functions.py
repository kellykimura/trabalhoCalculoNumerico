import numpy as np

# ===================== PARTE A =========================

def produto_escalar (mult1, mult2):

    produto = sum(mult1 * mult2)
    return produto

def polinomio2grau (x,y):
    # APROXIMAÇÃO POLINOMIAL DE GRAU 2
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
    
    # decomposição LU para resolver
    lu_fatorado = lu_factor(A)
    coeficientes = lu_solve(lu_fatorado, b)



    return coeficientes # retorna [a0, a1, a2]


# importar os dados da tabela para a variável dados
dados = np.loadtxt('Populacao_PresidentePrudente.dat')
x = dados[:,0]
y = dados[:,1]




