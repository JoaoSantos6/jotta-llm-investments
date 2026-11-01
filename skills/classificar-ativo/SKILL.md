---
nome: classificar-ativo
descricao: Enquadra cada ativo em saudável, atenção, em queda ou perigoso aplicando os critérios documentados, com justificativa e critérios disparados.
papel: agents/analista.md
entradas: session/dados/<ATIVO>.md, session/dados/macro.md, session/briefing.md
saidas: bloco "Classificação" em session/analise/<ATIVO>.md
---

# Skill — Classificar ativo

## Estados

| Estado | Significado (resumo) |
| --- | --- |
| 🟢 **Saudável** | Nenhum critério de alerta disparado com dados suficientes. |
| 🟡 **Atenção** | Ao menos um critério de *atenção* disparado. |
| 🟠 **Em queda** | Preço/rendimento em deterioração relevante (critérios *em queda*), com causa identificada ou a identificar. |
| 🔴 **Perigoso** | Ao menos um critério *perigoso* disparado. |

Critérios por classe: [`knowledge/sinais-de-alerta.md`](../../knowledge/sinais-de-alerta.md) e `knowledge/<classe>/criterios.md`.

## Algoritmo

1. Leia os critérios da classe e a tabela de sinais de alerta.
2. Para **cada critério**, marque: `disparado`, `não disparado` ou `dados insuficientes`, citando o dado (com `[n]` da fonte) que embasa a marcação.
3. Estado = **o mais grave** entre os critérios disparados (perigoso > em queda > atenção > saudável).
4. **Ajuste por setor/tipo**: aplique as exceções documentadas (ex.: bancos não usam dívida líq./EBITDA; FII de papel não usa vacância). Diga qual exceção aplicou.
5. **Em queda — ruído ou estrutural?** Se o critério *em queda* disparar, classifique a causa:
   - *ruído de mercado*: queda acompanha o índice/setor e os fundamentos (lucro, caixa, rendimento) não pioraram;
   - *estrutural*: fundamentos pioraram ou há evento específico negativo;
   - *indefinido*: dados insuficientes — diga o que falta.
6. **Confiança**: `alta` (todos os critérios com dado), `média` (até 2 com dados insuficientes), `baixa` (mais de 2). Com confiança baixa, escreva "classificação provisória".
7. **Perfil de qualidade (só ações).** Marque as sete dimensões de [`knowledge/acoes/qualidade.md`](../../knowledge/acoes/qualidade.md) (`forte`/`neutra`/`fraca`/`dados insuficientes`), cada uma com fato e fonte. O perfil **não altera o estado** — ele contextualiza. Exceção: Q1 com histórico curto limita a confiança a `média`.
8. **Múltiplo baixo com deterioração.** Se o múltiplo está abaixo da média histórica do ativo e algum critério de resultado (AC-03/04/05/09/10) disparou, registre isso na justificativa com a frase descritiva de `qualidade.md`.
9. **Relação com o briefing**: verifique a compatibilidade com objetivo, horizonte e risco do usuário (ex.: Tesouro IPCA+ 2045 com horizonte < 1 ano → critério *perigoso* de Tesouro). Isso é descrição de compatibilidade, nunca recomendação.

## Saída

```markdown
## Classificação
Estado: 🟡 Atenção · Confiança: média
Critérios disparados:
- [atenção] P/VP 1,22 > 1,15 [3]
- [atenção] 18% da receita com contratos vencendo em 12 meses [4]
Não disparados: vacância física 4% [4]; alavancagem 8% [5]
Dados insuficientes: duração média dos contratos (WAULT) — não encontrado em [4], [6]
Exceções aplicadas: nenhuma
Justificativa: …(2–4 frases, só fatos citados)
```

Para ações, acrescente logo abaixo:

```markdown
### Perfil de qualidade
| Dimensão | Marcação | Evidência |
| --- | --- | --- |
| Q1 Histórico de resultados | forte | Lucro positivo em 10 dos últimos 10 anos [7] |
| Q2 Rentabilidade vs. pares | neutra | ROE 12m de 14% vs. mediana de 13% de 3 pares [3][8] |
| Q3 Geração de caixa | fraca | FCO/lucro de 0,4 em 2025 e 0,5 em 2026 [5] |
| Q4 Gestão e alocação de capital | dados insuficientes | — |
| Q5 Governança e minoritário | forte | Novo Mercado, 4 de 7 conselheiros independentes [9] |
| Q6 Vantagens competitivas | neutra | … |
| Q7 Perenidade e ciclicidade | fraca | Setor cíclico (siderurgia) [setores.md] |
Porte: small cap (valor de mercado R$ 1,2 bi; fora do Ibovespa, no SMLL) [3][10]
```

Não use emojis fora do rótulo do estado.
