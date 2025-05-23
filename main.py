import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import functions
import teste_alinhamento

def salvar_grafico(x, y_real, y_aprox, titulo, nome_arquivo):
    plt.figure(figsize=(12, 8))
    plt.plot(x, y_real, 'ko', label='Dados Originais')
    plt.plot(x, y_aprox, label=titulo)
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.title(f'Ajuste: {titulo}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"plots/{nome_arquivo}.png", dpi=300)
    plt.close()


data = np.loadtxt("./data/Populacao_PresidentePrudente.dat")

anos = data[:,0]
populacao = data[:,1]

# Necessário normalizar por erro nos plots
anos_normalizado = anos - anos[0]

aprox_grau_2 = functions.ajustado_grau_2(anos_normalizado, populacao)
aprox_grau_3 = functions.ajustado_grau_3(anos_normalizado, populacao)
aprox_exp = functions.ajustado_exponencial(anos_normalizado, populacao)
aprox_geo = functions.ajustado_geometrica(anos_normalizado, populacao)
aprox_hiper = functions.ajustado_hiperbólica(anos_normalizado, populacao)

salvar_grafico(anos, populacao, aprox_grau_2, "Polinomial Grau 2", "polinomial_grau_2")
salvar_grafico(anos, populacao, aprox_grau_3, "Polinomial Grau 3", "polinomial_grau_3")
salvar_grafico(anos, populacao, aprox_exp, "Exponencial", "exponencial")
salvar_grafico(anos, populacao, aprox_hiper, "Hiperbólica", "hiperbolica")
salvar_grafico(anos, populacao, aprox_geo, "Geométrica", "geometrica")

resultados_r2 = {
    "Polinomial Grau 2": teste_alinhamento.teste_alinhamento_r2(populacao, aprox_grau_2),
    "Polinomial Grau 3": teste_alinhamento.teste_alinhamento_r2(populacao, aprox_grau_3),
    "Exponencial": teste_alinhamento.teste_alinhamento_r2(populacao, aprox_grau_3),
    "Geométrica": teste_alinhamento.teste_alinhamento_r2(populacao, aprox_geo),
    "Hiperbólica": teste_alinhamento.teste_alinhamento_r2(populacao, aprox_hiper),
}

df = pd.DataFrame(list(resultados_r2.items()), columns=["Função", "R²"])
print(df)
