"""
otimizacao_macroscopia.py
--------------------------------------------------------------
Autores:
- Caio Alexandre dos Santos (RM 558460)
- Italo Caliari Silva (RM 554758)
- Leandro do Nascimento Souza (RM 558893)
- Rafael de Mônaco Maniezo (RM 556079)
- Vinicius Rozas Pannucci de Paula Cont (RM 555338)

Problema:
Seleção de amostras macroscópicas para análise diária.

Cada amostra tem:
  - tempo_de_analise (min)
  - prioridade_clinica (valor de importância)

Objetivo:
Maximizar a soma das prioridades clínicas dentro de um tempo máximo (T).

Modelagem:
Problema da Mochila Binária (0/1 Knapsack)
"""

from typing import Dict, List, Tuple
import random

# ============================================================
# 🧩 1. Formulação do Problema
# ============================================================
# Estado: DP(i, t) → melhor prioridade possível usando amostras[i..N-1] com tempo t restante.
# Decisão: analisar ou não a amostra i.
# Transição: DP(i, t) = max(DP(i+1, t), prioridade[i] + DP(i+1, t - tempo[i])) se tempo[i] ≤ t
# Função objetivo: DP(0, T)

# ============================================================
# ⚙️ 2. Implementações Recursiva, Memoizada e Iterativa
# ============================================================

def selecionar_amostras_recursivo(amostras: List[Tuple[int, int]], tempo_total: int) -> int:
    """Versão recursiva pura (sem memoização) — custo exponencial, apenas didática."""
    N = len(amostras)

    def DP(i: int, t: int) -> int:
        if i == N or t <= 0:
            return 0
        tempo, prioridade = amostras[i]
        # Decisão: não analisar
        melhor = DP(i + 1, t)
        # Decisão: analisar (se couber no tempo)
        if tempo <= t:
            melhor = max(melhor, prioridade + DP(i + 1, t - tempo))
        return melhor

    return DP(0, tempo_total)


def selecionar_amostras_memo(amostras: List[Tuple[int, int]], tempo_total: int) -> Tuple[int, Dict[Tuple[int, int], int]]:
    """Versão recursiva com memoização (top-down)."""
    N = len(amostras)
    memo: Dict[Tuple[int, int], int] = {}

    def DP(i: int, t: int) -> int:
        if i == N or t <= 0:
            return 0
        if (i, t) in memo:
            return memo[(i, t)]

        tempo, prioridade = amostras[i]
        melhor = DP(i + 1, t)
        if tempo <= t:
            melhor = max(melhor, prioridade + DP(i + 1, t - tempo))

        memo[(i, t)] = melhor
        return melhor

    return DP(0, tempo_total), memo


def selecionar_amostras_iterativo(amostras: List[Tuple[int, int]], tempo_total: int) -> Tuple[int, List[List[int]]]:
    """Versão iterativa (bottom-up)."""
    N = len(amostras)
    dp = [[0] * (tempo_total + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        tempo, prioridade = amostras[i - 1]
        for t in range(tempo_total + 1):
            dp[i][t] = dp[i - 1][t]
            if tempo <= t:
                dp[i][t] = max(dp[i][t], prioridade + dp[i - 1][t - tempo])

    return dp[N][tempo_total], dp

# ============================================================
# 🔍 3. Reconstrução da Solução
# ============================================================

def reconstruir_memo(amostras: List[Tuple[int, int]], tempo_total: int, memo: Dict[Tuple[int, int], int]) -> List[int]:
    """Reconstrói as amostras escolhidas (usando memoização)."""
    N = len(amostras)
    escolhidas = []
    i, t = 0, tempo_total

    while i < N and t > 0:
        val_atual = memo.get((i, t), 0)
        val_sem = memo.get((i + 1, t), 0)
        if val_atual == val_sem:
            i += 1
        else:
            escolhidas.append(i)
            tempo, _ = amostras[i]
            t -= tempo
            i += 1

    return escolhidas


def reconstruir_iterativo(amostras: List[Tuple[int, int]], tempo_total: int, dp: List[List[int]]) -> List[int]:
    """Reconstrói as amostras escolhidas (usando tabela bottom-up)."""
    N = len(amostras)
    escolhidas = []
    i, t = N, tempo_total

    while i > 0 and t > 0:
        if dp[i][t] != dp[i - 1][t]:
            escolhidas.append(i - 1)
            tempo, _ = amostras[i - 1]
            t -= tempo
        i -= 1

    escolhidas.reverse()
    return escolhidas

# ============================================================
# 🧪 4. Comparação e Testes
# ============================================================

def comparar_abordagens(amostras: List[Tuple[int, int]], tempo_total: int, verbose=True):
    """Compara top-down e bottom-up, garantindo resultados idênticos."""
    valor_memo, memo = selecionar_amostras_memo(amostras, tempo_total)
    valor_iter, dp = selecionar_amostras_iterativo(amostras, tempo_total)

    escolhidas_memo = reconstruir_memo(amostras, tempo_total, memo)
    escolhidas_iter = reconstruir_iterativo(amostras, tempo_total, dp)

    assert valor_memo == valor_iter, "❌ Erro: resultados diferentes entre top-down e bottom-up!"

    if verbose:
        print("\n🧬 Amostras disponíveis:")
        for i, (t, p) in enumerate(amostras):
            print(f"  {i}. Tempo: {t:3d} min | Prioridade: {p}")

        print(f"\n⏱️ Tempo total disponível: {tempo_total} min")
        print(f"⭐ Resultado ótimo: {valor_memo}")
        print(f"📦 Amostras escolhidas (memo): {escolhidas_memo}")
        print(f"📦 Amostras escolhidas (iterativo): {escolhidas_iter}")
        print("\n✅ Ambas as versões produziram o mesmo resultado!")

# ============================================================
# 🚀 5. Execução Principal
# ============================================================

if __name__ == "__main__":
    # Exemplo fixo
    amostras_exemplo = [
        (30, 10),   # Amostra A
        (40, 20),   # Amostra B
        (60, 30),   # Amostra C
        (90, 50),   # Amostra D
        (120, 70)   # Amostra E
    ]
    tempo_disponivel = 180

    comparar_abordagens(amostras_exemplo, tempo_disponivel)

    # Testes automáticos
    print("\n🔁 Testes automáticos (verificando equivalência)...")
    for _ in range(5):
        n = 8
        amostras = [(random.randint(10, 100), random.randint(5, 80)) for _ in range(n)]
        tempo = random.randint(100, 300)
        valor1, _ = selecionar_amostras_memo(amostras, tempo)
        valor2, _ = selecionar_amostras_iterativo(amostras, tempo)
        assert valor1 == valor2, "Falha em teste automático!"
    print("✅ Todos os testes passaram com sucesso!")
