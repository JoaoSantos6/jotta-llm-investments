---
nome: gerar-relatorio
descricao: Renderiza o relatório aprovado no formato pedido — chat, HTML autocontido ou PDF.
papel: agents/orquestrador.md
entradas: session/relatorio.md (aprovado), session/briefing.md
saidas: resposta no chat, session/relatorio.html e/ou session/relatorio.pdf
---

# Skill — Gerar relatório

**Pré-condição:** `session/revisao.md` com `veredito: APROVADO`. Os renderizadores **não alteram conteúdo** — só formato. Nenhum fato novo entra nesta etapa.

## Chat

Siga [`templates/relatorio-chat.md`](../../templates/relatorio-chat.md):
1. "Em resumo" e tabela-síntese no topo (ativo · situação · em uma frase).
2. O que merece atenção (até 5 itens, cada um explicado).
3. Por ativo: detalhe *resumido* = em resumo + desempenho + saúde financeira + por que essa situação + até 3 riscos + o que acompanhar; *completo* = todas as seções do relatório.
4. O que a análise não cobriu, fontes e aviso legal no fim.

Sempre envie a versão chat (mesmo que o formato seja HTML/PDF), como resumo.

## HTML

1. Copie [`templates/relatorio.html`](../../templates/relatorio.html) para `session/relatorio.html`.
2. Substitua cada marcador `{{...}}` conforme os comentários do template. Converta o markdown do relatório para HTML simples (`<h3>`, `<p>`, `<ul>`, `<table>`); escape `<`, `>` e `&` no texto.
3. O arquivo deve ser **autocontido**: sem CSS/JS/fontes externas, sem imagens remotas.
4. Confira que nenhum `{{` sobrou no arquivo.

## PDF

Em ordem de preferência:
1. **Script:** `python scripts/gerar_pdf.py session/relatorio.html` (usa Chrome/Edge/Chromium headless já instalado; sem dependências Python).
2. **Ferramenta nativa** da LLM, se houver (ex.: geração de PDF embutida), a partir do mesmo HTML.
3. **Manual:** se nada funcionar, entregue o HTML e oriente: "abra no navegador → Imprimir → Salvar como PDF".

## Encerramento

A resposta termina no aviso legal. Se houve HTML/PDF, uma linha antes dele com os caminhos gerados (`session/relatorio.html`, `.pdf`). Não acrescente "próximos passos", ofertas de aprofundamento nem perguntas (`rules/escrita.md`).
