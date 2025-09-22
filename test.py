from itertools import product

# Valores e pesos
valores = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
pesos = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]
capacidade_maxima = 878
dim = len(valores)

melhor_valor = 0
melhor_selecao = []

# Testar todas as combinações possíveis (2^20)
for selecao in product([0, 1], repeat=dim):
    peso_total = sum(p for p, s in zip(pesos, selecao) if s)
    valor_total = sum(v for v, s in zip(valores, selecao) if s)

    if peso_total <= capacidade_maxima and valor_total > melhor_valor:
        melhor_valor = valor_total
        melhor_selecao = selecao

print(f"Valor máximo possível: {melhor_valor}")
print(f"Seleção ótima: {melhor_selecao}")
