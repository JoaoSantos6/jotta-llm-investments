# jotta-llm-investments

Framework em markdown que transforma qualquer LLM com acesso a arquivos e à web em um **analista de carteiras da B3** — ações, FIIs e Tesouro Direto.

Não é app, site nem API: é um conjunto de **rules**, **skills**, **agentes** e uma **base de conhecimento** que a LLM lê e segue. Ela entrevista você, busca dados atuais com fonte e data, aplica critérios documentados por classe de ativo e entrega um relatório no chat, em HTML ou em PDF.

> ⚠️ Material informativo. Não é recomendação de investimento nem consultoria (Resoluções CVM 19 e 20). Veja [`templates/disclaimer.md`](templates/disclaimer.md).

## Como usar

1. Clone o repositório e abra a pasta em uma LLM com acesso a arquivos e à web:
   - **Claude Code:** `claude` na pasta (lê `CLAUDE.md`).
   - **Cursor:** abra a pasta (lê `.cursor/rules/jotta-llm-investments.mdc`).
   - **Codex / outras:** leem `AGENTS.md`. No ChatGPT, conecte o repositório e peça para seguir o `AGENTS.md`.
2. Peça: **"Analise minha carteira: PETR4, ITUB4, HGLG11, MXRF11 e Tesouro IPCA+ 2035."**
3. Responda à entrevista curta (uma pergunta por vez, ~5 min) e confirme o briefing.
4. Receba o relatório. Tudo fica em `session/` (fora do git).

## O que você recebe

**Primeiro, a resposta:** um resumo de poucas frases dizendo quais ativos estão bem, quais pedem atenção e qual a principal ameaça. Os detalhes vêm depois, e cada número vem explicado: o que ele mede e por que é bom ou ruim.

**Por ativo:** situação (🟢 saudável · 🟡 atenção · 🟠 em queda · 🔴 perigoso) e por quê, como está hoje, o que vem pela frente em 3–12 meses, setor e cenário, o que pode mudar o quadro, riscos e o que acompanhar.

**Da carteira:** concentração por ativo, setor e classe; exposição a juros, inflação e câmbio; correlações; compatibilidade com seu objetivo e horizonte; alertas priorizados.

**Sempre:** toda afirmação factual com fonte e data de coleta, e revisão automática contra tom de recomendação.

## Como funciona

```
grill-me → briefing confirmado → coleta (macro + ações + FIIs + Tesouro) → classificação
→ análise por ativo + consolidada → revisor (aprova ou devolve) → chat / HTML / PDF
```

| Pasta | Conteúdo |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Ponto de entrada (adaptadores: `CLAUDE.md`, `.cursor/rules/`) |
| [`rules/`](rules) | O que nunca pode acontecer: compliance CVM, fontes, fluxo, privacidade, escrita para o leitor |
| [`skills/`](skills) | Como fazer cada etapa (`<skill>/SKILL.md`) |
| [`agents/`](agents) | Papéis: orquestrador, pesquisadores por classe, analista, revisor |
| [`knowledge/`](knowledge) | Critérios por classe, sinais de alerta, fontes, glossário |
| [`templates/`](templates) | Briefing, dados coletados, relatório (md, chat, HTML), disclaimer |
| [`scripts/`](scripts) | `gerar_pdf.py` (HTML → PDF) e `validar_repo.py` (consistência) |
| [`tests/`](tests) | Sessões de teste com comportamento esperado |
| [`docs/PRD.md`](docs/PRD.md) | Documento de requisitos |

## Requisitos

- Uma LLM com leitura de arquivos e busca/leitura de páginas web.
- Para PDF via script: Python 3.8+ e Chrome, Edge ou Chromium instalado.
- Nenhuma API paga.

## Contribuir

Veja [`CONTRIBUTING.md`](CONTRIBUTING.md). Antes de abrir PR: `python scripts/validar_repo.py`.

## Licença

[MIT](LICENSE).
