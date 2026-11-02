# CLAUDE.md

Este repositório é agnóstico de LLM. Todas as instruções estão em [`AGENTS.md`](AGENTS.md) — leia-o e siga-o integralmente.

@AGENTS.md

## Específico do Claude Code

- Use a ferramenta de subagentes (Agent/Task) para rodar os pesquisadores de `agents/` em paralelo; cada subagente recebe o caminho do seu arquivo de agente, o `session/briefing.md` e a lista de ativos do seu lote.
- Use WebSearch/WebFetch para a coleta, sempre respeitando `knowledge/fontes.md`.
- Para PDF, prefira `python scripts/gerar_pdf.py session/relatorio-AAAA-MM-DD-HHMM-ATIVOS.html` (nome do arquivo em `skills/gerar-relatorio`).
- Em HTML/PDF, envie o arquivo com `SendUserFile` e responda só com ele e o aviso legal.
