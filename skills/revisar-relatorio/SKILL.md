---
nome: revisar-relatorio
descricao: Confere fontes, linguagem e completude do relatório; aprova ou reprova com apontamentos objetivos.
papel: agents/revisor.md
entradas: session/relatorio.md, session/analise/*.md, session/dados/*.md, session/briefing.md
saidas: session/revisao.md com veredito APROVADO ou REPROVADO
---

# Skill — Revisar relatório

Assuma o papel de [`agents/revisor.md`](../../agents/revisor.md). Você **não reescreve** o relatório; você aponta.

## Checklist (todos obrigatórios)

### A. Fontes (bloqueante)
- [ ] A1. Todo número e todo fato tem `[n]`.
- [ ] A2. Todo `[n]` existe na lista de fontes, com URL, data de referência e data de coleta.
- [ ] A3. Amostra: confira **pelo menos 5 números** (ou todos, se houver menos) contra `session/dados/*.md` — valor, fonte e datas batem.
- [ ] A4. Nenhum número aparece no relatório sem estar em `session/dados/` (ou ser conta simples mostrada).

### B. Linguagem / compliance (bloqueante)
- [ ] B1. Nenhum termo da tabela "Proibido" de `rules/compliance-cvm.md`, nem sinônimos.
- [ ] B2. Nenhum preço-alvo, valor justo ou alocação própria.
- [ ] B3. Previsões estão no condicional e ligadas a gatilhos.
- [ ] B4. Consenso/recomendação de terceiros está identificado (quem, quando, onde).
- [ ] B5. Disclaimer de `templates/disclaimer.md` presente e sem alterações.
- [ ] B6. Múltiplos aparecem comparados a histórico/pares, com a conclusão descritiva sobre o que o preço embute (`knowledge/leitura-de-indicadores.md` › seção 6), sem "barato", "caro", "descontado", "esticado" ou equivalentes.
- [ ] B7. Perfil de qualidade não é convertido em nota, ranking ou conclusão de investimento ("empresa de qualidade, vale a pena").

### C. Completude (bloqueante)
- [ ] C1. Todos os ativos do foco do briefing estão no relatório.
- [ ] C2. Cada ativo tem as seções fixas, nenhuma vazia: no relatório, as do template; em `session/analise/<ATIVO>.md`, as 8 da análise.
- [ ] C3. Cada classificação em `session/analise/` lista critérios disparados e justificativa, e cada sinal que define a situação aparece explicado no relatório.
- [ ] C4. Consolidada presente quando o foco é "carteira toda" ou "uma classe".
- [ ] C5. Preocupações do briefing foram respondidas.
- [ ] C6. Cada ação tem, em `session/analise/`, o perfil de qualidade Q1–Q7 (dimensões sem dado marcadas como `dados insuficientes`) e os critérios AC-01 a AC-14 avaliados.
- [ ] C7. As perguntas em aberto da análise foram levantadas no aprofundamento ou aparecem em "O que esta análise não cobriu".

### E. Leitura (bloqueante — ver `rules/escrita.md`)
- [ ] E1. Nenhum código interno (AC-, FI-, FT-, FP-, TD-, CA-, Q1–Q7), nenhum "critério disparado/não disparado", "limiar do framework", "classificação provisória" ou nome de arquivo do repositório no relatório.
- [ ] E2. O relatório e cada ativo abrem com uma resposta direta: está bem ou não, e qual a principal ameaça à frente.
- [ ] E3. Todo número usado para justificar situação, alerta ou risco vem com o que ele mede e por que importa. Teste: um leigo entenderia por que esse número é bom ou ruim sem pesquisar?
- [ ] E4. Nada depois do aviso legal; sem "próximos passos", ofertas ("posso aprofundar", "quer que eu…") ou perguntas ao usuário.
- [ ] E5. Sem glossário em bloco e sem listas do que não acendeu alerta; contas intermediárias e divergências entre fontes fora do corpo do texto.
- [ ] E6. Nenhuma lista de números soltos: cada indicador em "Como está hoje" e no cenário econômico tem referência (histórico, mediana do setor com pares nomeados ou índice), leitura e conclusão. Cada dado macro diz qual ativo da carteira afeta.
- [ ] E7. Cada ativo tem desempenho em 1 semana, 12 meses e 5 anos contra o índice de referência, e a conclusão de saúde financeira (sólida / com pontos de atenção / frágil) — ou a lacuna explicada.
- [ ] E8. Sem especulação ("provavelmente", "parece que") e sem narrar a coleta no corpo do texto ("não consegui ler…").

### F. Brevidade inteligente (bloqueante — ver `rules/escrita.md`, seção 2a)
- [ ] F1. O relatório tem as duas partes, nesta ordem: "Leitura rápida" (inteira) e depois "Saiba mais".
- [ ] F2. Cada ativo tem um cartão na leitura rápida com os quatro rótulos, nesta ordem: "Em uma linha", "Por que importa", "Em números" e "O que observar". A carteira tem "Em uma linha" e "Por que importa".
- [ ] F3. Limites de tamanho, contados sem as referências `[n]`:
  - cartão de cada ativo: até 80 palavras;
  - "Em resumo" da carteira: até 60 palavras, mais a tabela;
  - cada item de atenção: até 40 palavras;
  - "Em números": até 3 itens.
- [ ] F4. A leitura rápida não tem tabelas além da síntese, nem contas ou listas de indicadores. Cada número dela traz, na mesma linha, o que significa e se é bom ou ruim.
- [ ] F5. Coerência entre as camadas:
  - a leitura rápida não contradiz o "Saiba mais";
  - todo fato da leitura rápida reaparece, com o detalhe, no "Saiba mais" do mesmo ativo ou tema;
  - leitura provisória e lacunas que mudam a conclusão estão já na leitura rápida.
- [ ] F6. O "Saiba mais" tem todas as seções obrigatórias (C2). Nada foi cortado em nome da brevidade.

### D. Qualidade (não bloqueante — gera recomendação de melhoria)
- [ ] D1. Termos técnicos explicados na primeira ocorrência.
- [ ] D4. Frases longas ou parágrafos com mais de 4 linhas que poderiam ser quebrados.
- [ ] D2. Lacunas de dados declaradas.
- [ ] D3. Números no padrão brasileiro.

## Veredito

- **APROVADO**: todos os itens A, B, C, E e F marcados.
- **REPROVADO**: qualquer item A, B, C, E ou F falhou.

Grave `session/revisao.md`:

```markdown
---
ciclo: 1
veredito: REPROVADO
---
## Apontamentos bloqueantes
1. [B1] Seção HGLG11 › Expectativa: "momento de oportunidade" → linguagem de recomendação. Trecho: "…"
2. [A1] Seção PETR4 › Estado atual: "dividend yield de 14%" sem fonte.
3. [E3] Seção TAEE4 › Riscos: "dívida líquida/EBITDA de 4,2x" sem dizer o que mede nem por que é um risco.
## Melhorias (não bloqueantes)
1. [D1] "WAULT" não explicado.
```

Cada apontamento: código do item, local exato, trecho e motivo. Com REPROVADO, devolva ao analista; com APROVADO, libere a entrega.
