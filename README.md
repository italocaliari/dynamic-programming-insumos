# ⚗️ Programação Dinâmica – Otimização de Insumos

Projeto desenvolvido para o **Desafio Acadêmico da DASA (FIAP 2025)**, aplicando **programação dinâmica** para otimizar o **uso e seleção de insumos (reagentes e aplicações)** em unidades de diagnóstico.

---

## 👥 Autores

- **Caio Alexandre dos Santos** (RM 558460)  
- **Italo Caliari Silva** (RM 554758)  
- **Leandro do Nascimento Souza** (RM 558893)  
- **Rafael de Mônaco Maniezo** (RM 556079)  
- **Vinicius Rozas Pannucci de Paula Cont** (RM 555338)

---

## 🧩 Problema

Cada insumo (ou amostra) possui:
- `tempo_de_analise` (em minutos)  
- `prioridade_clinica` (grau de importância)

O desafio consiste em **selecionar o conjunto ideal de insumos a serem processados**, de modo que a soma das **prioridades clínicas seja máxima**, respeitando um **tempo limite disponível (T)**.

---

## ⚙️ Formulação Matemática

O problema é modelado como o **Problema da Mochila Binária (0/1 Knapsack)**:

$$
\text{Maximizar} \quad \sum p_i x_i \quad \text{sujeito a} \quad \sum t_i x_i \leq T, \quad x_i \in \{0,1\}
$$

Onde:
- $p_i$ = prioridade clínica  
- $t_i$ = tempo de análise  
- $x_i$ = decisão (1 se o insumo é analisado, 0 caso contrário)

---

## 🧮 Abordagens Implementadas

| Versão | Descrição | Complexidade |
|--------|------------|--------------|
| `selecionar_amostras_recursivo` | Recursiva pura (didática, sem otimização) | Exponencial |
| `selecionar_amostras_memo` | Programação dinâmica top-down (memoização) | $O(N \times T)$ |
| `selecionar_amostras_iterativo` | Programação dinâmica bottom-up (tabela iterativa) | $O(N \times T)$ |

---

## 🔍 Reconstrução da Solução

Funções adicionais permitem **reconstruir quais insumos foram escolhidos** em cada versão (`memo` e `iterativa`), validando os resultados e garantindo **otimização e consistência**.

---

## 🚀 Execução do Código

### 1️⃣ Requisitos
- Python 3.8+
- Nenhuma biblioteca externa é necessária

### 2️⃣ Rodando o código
No terminal (VS Code ou CMD), execute:

```bash
python otimizacao_macroscopia.py
