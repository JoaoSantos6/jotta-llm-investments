# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versões seguem [SemVer](https://semver.org/lang/pt-BR/).

## [1.3.0] — 2026-10-31

Do número à conclusão: o relatório compara e conclui, em vez de listar dados.

### Adicionado
- `knowledge/leitura-de-indicadores.md`: referências (mediana de 3+ pares, índices setoriais da B3, IFIX, CDI), faixa "em linha", leitura favorável/em linha/desfavorável, tabelas de indicadores de ações e FIIs com a conclusão que cada um permite, conclusões descritivas para múltiplos e P/VP, e a síntese de saúde financeira (sólida, com pontos de atenção, frágil).
- Desempenho em 1 semana, 12 meses e 5 anos contra índice de mercado e do setor; desempenho da carteira contra o CDI.
- Itens E6–E8 no checklist do revisor (sem números soltos, desempenho e saúde presentes, sem especulação nem bastidores da coleta).

### Alterado
- Pesquisadores coletam variação em três janelas, índice do setor, indicadores de 3–5 pares e CDI acumulado.
- Templates: "Como está hoje" com tabelas de desempenho e saúde financeira, ambas com leitura e conclusão; cenário econômico liga cada dado a um ativo da carteira.
- Compliance permite concluir sobre saúde financeira e sobre o que o preço embute, mantendo a proibição de "barato/caro".

## [1.2.0] — 2026-10-31

Relatório escrito para o investidor, não para o framework.

### Adicionado
- `rules/escrita.md`: o framework é invisível no texto ao usuário (sem códigos como AC-02 ou Q3), conclusão primeiro e todo número com o que mede e por que importa. A entrega termina no aviso legal, sem "próximos passos".
- Etapa de **aprofundamento** antes da revisão: o analista registra perguntas em aberto e o orquestrador faz uma coleta pontual em vez de oferecer isso ao usuário no fim.
- Itens E1–E5 (leitura, bloqueantes), C7 e D4 no checklist do revisor.
- Checagem no `validar_repo.py`: templates do leitor não podem conter códigos internos.
- Sessão de teste 07 (leitura do relatório), agora obrigatória para aprovar uma LLM.

### Alterado
- Templates do relatório (markdown, chat e HTML) reorganizados: "Em resumo", "O que merece sua atenção", ativo por ativo (com "Por que essa situação"), carteira como um todo, cenário econômico e "O que esta análise não cobriu".
- Arquivos de `session/analise/` continuam técnicos; o relatório é a tradução para o investidor.
- Exemplos de linguagem em `rules/compliance-cvm.md` e `knowledge/sinais-de-alerta.md` sem jargão interno.

## [1.1.0] — 2026-10-31

Aprofundamento da análise de ações.

### Adicionado
- `knowledge/acoes/qualidade.md`: perfil de qualidade em sete dimensões (Q1–Q7), vantagens competitivas, taxonomia de riscos (sistêmicos × específicos), definição de small cap e regras para citar múltiplos em contexto.
- Critérios AC-09 (cobertura de juros), AC-10 (qualidade do lucro), AC-11 (coerência lucro × proventos), AC-12 (concentração de clientes), AC-13 (diluição) e AC-14 (partes relacionadas).
- Exceções para small caps e setores intensivos em capital; indicadores operacionais por setor; distinção entre negócios intensivos em capital e *asset light*.
- Formulário de Referência, DFP/ITR e índices da B3 como fontes; regras para agregar consenso de várias casas.
- Itens B6, B7 e C6 no checklist do revisor; regras de compliance para métodos de triagem e juízo sobre múltiplos.
- `knowledge/referencias.md` e sessão de teste 06.

### Alterado
- Pesquisador de ações coleta fluxo de caixa, despesa financeira, número de ações, múltiplos históricos e de pares, e dados qualitativos do Formulário de Referência.
- Estado "saudável" de ações exige 9 dos 14 critérios com dados.

## [1.0.0] — 2026-10-31

Primeira versão completa do MVP (roadmap v0.1 a v1.0 do PRD).

### Adicionado
- Ponto de entrada `AGENTS.md` e adaptadores `CLAUDE.md` e `.cursor/rules/jotta-llm-investments.mdc`.
- Rules: princípios, compliance CVM, fontes e dados, fluxo e portas, privacidade.
- Skills: `orquestrar-sessao`, `grill-me`, `coletar-dados`, `classificar-ativo`, `analisar-carteira`, `revisar-relatorio`, `gerar-relatorio`.
- Agentes: orquestrador, pesquisadores (ações, FIIs, Tesouro, macro), analista, revisor.
- Base de conhecimento: sinais de alerta; critérios de ações (com exceções por setor), FIIs (tijolo, papel, FOF, híbridos), Tesouro Direto, macro e carteira; setores; tipos de FII; fontes com fallback; glossário.
- Templates: briefing, dados coletados, relatório canônico, relatório para chat, relatório HTML autocontido, disclaimer.
- Scripts: `gerar_pdf.py` (Chromium headless, sem dependências) e `validar_repo.py`.
- Sessões de teste 01–05 e workflow de CI.
