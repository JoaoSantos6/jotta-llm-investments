---
nome: analisar-carteira
descricao: Produz a análise por ativo (seções fixas) e a análise consolidada da carteira, sem tom de recomendação.
papel: agents/analista.md
entradas: session/briefing.md, session/dados/*.md, classificações
saidas: session/analise/<ATIVO>.md, session/analise/consolidada.md, session/relatorio.md
---

# Skill — Analisar carteira

Há duas camadas de texto:

- **Arquivos de trabalho** (`session/analise/`): técnicos e completos, com códigos de critério, contas e tudo o que não disparou. Servem ao revisor.
- **Relatório** (`session/relatorio.md`): escrito para o investidor, seguindo [`rules/escrita.md`](../../rules/escrita.md). Nenhum código interno chega lá.

## Parte 1 — Por ativo (`session/analise/<ATIVO>.md`)

Seções **fixas e nesta ordem** (nenhuma pode ficar vazia; se faltar dado, escreva o que falta e por quê):

1. **Classificação** — saída de `skills/classificar-ativo`.
2. **Estado atual** — siga [`knowledge/leitura-de-indicadores.md`](../../knowledge/leitura-de-indicadores.md): todo indicador comparado com uma referência e com leitura `favorável`/`em linha`/`desfavorável`.
   - **Desempenho** em 1 semana, 12 meses e 5 anos contra o índice de referência e o do setor, com a leitura de cada janela e uma frase sobre a trajetória.
   - **Saúde financeira**: os pilares da classe contra a mediana dos pares (nomeados), com a conclusão `sólida`, `com pontos de atenção` ou `frágil`.
   - Último resultado contra o mesmo período do ano anterior, e o que ele indica.
   Para ações, inclua também:
   - o **perfil de qualidade** (tabela Q1–Q7 da classificação);
   - **múltiplos em contexto**: valor atual, média histórica do próprio ativo e mediana dos pares, com a conclusão sobre o que o preço embute, sem "barato/caro" (ver `knowledge/leitura-de-indicadores.md` › seção 6);
   - 2–3 **indicadores operacionais** do setor e sua tendência.
3. **Expectativa 3–12 meses** — o que o calendário e o consenso público indicam: próximos resultados, vencimentos de contrato, decisões do Copom, guidance da empresa, consenso de terceiros (identificado). Sem previsão própria.
4. **Cenário do setor/mercado** — como o setor está, com ligação ao `macro.md`.
5. **Impactos possíveis** — tabela `Fator | Tipo (macro/regulatório/específico) | Efeito possível | Gatilho observável`.
6. **Riscos** — lista priorizada (maior impacto primeiro), cada risco ligado a um fato citado. Para ações, rotule cada risco com a categoria da taxonomia de `knowledge/acoes/qualidade.md` (ex.: *[alavancagem]*, *[regulatório]*, *[sistêmico: juros]*), começando pelos específicos.
7. **O que monitorar** — 3–5 indicadores/eventos concretos com data ou periodicidade.
8. **Perguntas em aberto** — até 2 dúvidas que um levantamento a mais resolveria e que mudariam a leitura do usuário (ex.: "queda de 14% em outubro sem causa nas fontes lidas"; "dívida da aquisição não divulgada"). Para cada uma: o que buscar e onde. Escreva "nenhuma" se não houver. O orquestrador usa esta seção no aprofundamento.

Para cada risco e cada sinal, anote também **por que importa** (a consequência possível para resultado, proventos ou preço). Essa frase é a matéria-prima da explicação no relatório.

Se o usuário declarou uma preocupação específica (briefing item 6) que toca este ativo, responda-a explicitamente dentro de "Riscos" ou "Impactos".

## Parte 2 — Consolidada (`session/analise/consolidada.md`)

Use [`knowledge/carteira/criterios.md`](../../knowledge/carteira/criterios.md):

1. **Tabela-síntese** — ativo, classe, setor/segmento, peso, estado, principal alerta.
2. **Concentração** — por ativo, setor e classe; limiares disparados. Sem pesos informados: use pesos iguais e diga isso.
3. **Exposição macro** — juros (Selic/curva), inflação (IPCA), câmbio; para cada fator, quais ativos são sensíveis e em que direção (ver `knowledge/macro/criterios.md`). No cenário econômico do relatório, cada dado macro termina dizendo qual ativo afeta.
   - **Desempenho da carteira** — com pesos, retorno ponderado em 12 meses e 5 anos contra o CDI acumulado; sem pesos, diga que usou pesos iguais.
4. **Correlações óbvias** — ativos expostos ao mesmo risco (ex.: dois bancos; FIIs de papel + Tesouro Selic ambos atrelados a juros pós).
   - **Perfil das ações da carteira** — parcela em small caps, em setores cíclicos (Q7 fraca) e em empresas com geração de caixa fraca (Q3 fraca), com os pesos.
5. **Compatibilidade com o briefing** — objetivo, horizonte e tolerância a risco vs. composição (descritivo).
6. **Alertas priorizados** — no máximo 5, do mais grave ao menos grave, cada um com ativo(s), critério, fonte e por que importa.
7. **Perguntas em aberto** — como na Parte 1, para dúvidas da carteira como um todo.

## Parte 3 — Montagem (`session/relatorio.md`)

Monte o relatório canônico a partir de [`templates/relatorio.md`](../../templates/relatorio.md). É este arquivo que o revisor avalia e do qual todos os formatos de saída derivam. Fontes numeradas `[n]` são únicas para o relatório inteiro.

Aqui você **traduz** a análise para o investidor (`rules/escrita.md`). O relatório tem duas partes (seção 2a da rule): **Leitura rápida** e **Saiba mais**.

1. Escreva primeiro o "Saiba mais" de cada ativo, completo, a partir do arquivo de análise. Depois **destile** a leitura rápida a partir dele: o cartão de cada ativo e o "Em resumo" da carteira, com os rótulos fixos (em uma linha, por que importa, em números, o que observar) e dentro dos limites de palavras. Destilar é escolher o que mais importa, não reescrever: a leitura rápida não traz fato que o "Saiba mais" não sustente.
2. Converta cada critério disparado em um sinal explicado: fato, o que mede, comparação com a referência e consequência possível. Ex.: AC-02 disparado vira "a dívida equivale a 4,2 anos da geração de caixa da operação; para uma transmissora, acima de 4 vezes é alto, e mais caixa vai para juros em vez de dividendos".
3. Critérios não disparados viram, no máximo, uma frase sobre o que está em ordem. Dados insuficientes viram uma frase sobre o que faltou e o efeito na leitura.
4. Contas e reconstruções ficam no arquivo de análise; no relatório, só o resultado com a fonte.
5. Se o briefing traz uma preocupação declarada, responda-a de forma direta no "Em resumo" (da carteira ou do ativo envolvido).

Correspondência entre as seções da análise e do relatório:

| Arquivo de análise | Relatório |
| --- | --- |
| Classificação + principal sinal + o evento mais próximo | Cartão do ativo na **Leitura rápida** (em uma linha, por que importa, em números, o que observar) |
| Classificação | Situação no título + "Por que essa situação" (no "Saiba mais") |
| Estado atual (desempenho, saúde financeira, perfil Q1–Q7, múltiplos) | "Como está hoje": "Desempenho", "Saúde financeira", "Qualidade do negócio", "Preço em relação a lucro e patrimônio" |
| Expectativa 3–12 meses | "O que vem pela frente" |
| Cenário do setor/mercado | "Setor e cenário" |
| Impactos possíveis | "O que pode mudar o quadro" |
| Riscos | "Riscos" (rótulo de categoria vira o nome do risco em linguagem comum) |
| O que monitorar | "O que acompanhar" |
| Perguntas em aberto não resolvidas, lacunas | "Limites desta leitura" (até 3, as que mudam a conclusão) + "Saiba mais: o que esta análise não cobriu" (lista completa) |
| Consolidada (concentração e fator de mercado mais relevante) | "Carteira e cenário" na leitura rápida + "Saiba mais: a carteira como um todo" e "Saiba mais: cenário econômico" |

## Tom

Releia `rules/compliance-cvm.md` e `rules/escrita.md` antes de escrever. Verbos descritivos: "registra", "apresenta", "dispara", "está exposto a", "pode". Nunca: "deve", "recomendo", "vale a pena", "oportunidade".
