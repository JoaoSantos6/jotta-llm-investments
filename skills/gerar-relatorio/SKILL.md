---
nome: gerar-relatorio
descricao: Renderiza o relatório aprovado no formato pedido — chat, HTML autocontido ou PDF.
papel: agents/orquestrador.md
entradas: session/relatorio.md (aprovado), session/briefing.md
saidas: resposta no chat, session/relatorio.html e/ou session/relatorio.pdf
---

# Skill — Gerar relatório

**Pré-condição:** `session/revisao.md` com `veredito: APROVADO`. Os renderizadores **não alteram conteúdo** — só formato. Nenhum fato novo entra nesta etapa.

## Brevidade inteligente nos três formatos

O relatório canônico já vem em duas partes, "Leitura rápida" e "Saiba mais" (`rules/escrita.md`, seção 2a). Os renderizadores preservam essa ordem:

- a leitura rápida inteira vem antes de qualquer detalhe;
- o "Saiba mais" contém todo o detalhe;
- nenhum formato mistura tabelas densas na leitura rápida.

## Chat

Siga [`templates/relatorio-chat.md`](../../templates/relatorio-chat.md):
1. Leitura rápida, sempre: "Em uma linha" e "Por que importa" da carteira, tabela-síntese (ativo · situação · em uma frase), o que merece atenção (até 5 itens curtos), um cartão por ativo (em uma linha, por que importa, em números, o que observar), carteira e cenário, limites desta leitura.
2. Detalhe *resumido*: termina aí, com fontes e aviso legal.
3. Detalhe *completo*: depois de toda a leitura rápida, um bloco "Saiba mais" com todas as seções do relatório canônico, ativo por ativo, e depois carteira, cenário e a lista completa do que a análise não cobriu.
4. Fontes e aviso legal no fim.

Sempre envie a versão chat (mesmo que o formato seja HTML/PDF), como resumo. Nesse caso, envie só a leitura rápida e diga numa linha onde está o detalhe (o arquivo HTML/PDF).

## HTML

1. Copie [`templates/relatorio.html`](../../templates/relatorio.html) para `session/relatorio.html`.
2. Substitua cada marcador `{{...}}` conforme os comentários do template. Converta o markdown do relatório para HTML simples (`<h3>`, `<h4>`, `<p>`, `<ul>`, `<table>`); escape `<`, `>` e `&` no texto.
3. Interatividade obrigatória:
   - cada cartão de ativo tem um **botão "Saiba mais"** (`aria-controls="d-TICKER"`) que abre o detalhe do ativo, e cada detalhe tem o link "Voltar à leitura rápida";
   - as linhas da tabela-síntese levam `data-alvo="d-TICKER"`;
   - as referências `[n]` levam `data-n`, para mostrar a fonte ao clicar.

   O script do template já faz o resto: abrir e fechar detalhes, abrir todos, tema, impressão e tempo de leitura.
4. O arquivo deve ser **autocontido**: CSS e JS inline, sem CSS/JS/fontes externas, sem imagens remotas. Sem JavaScript, todo o detalhe aparece aberto, então nada se perde.
5. Confira que nenhum `{{` sobrou no arquivo e que cada `aria-controls` aponta para um `id` existente.

## PDF

O PDF sai do mesmo HTML. Na impressão, o template abre todo o detalhe e põe a leitura rápida nas primeiras páginas. A "Parte 2 · Saiba mais" começa em página nova, com cada ativo em página própria. Botões e barra de topo não aparecem no papel.


Em ordem de preferência:
1. **Script:** `python scripts/gerar_pdf.py session/relatorio.html` (usa Chrome/Edge/Chromium headless já instalado; sem dependências Python).
2. **Ferramenta nativa** da LLM, se houver (ex.: geração de PDF embutida), a partir do mesmo HTML.
3. **Manual:** se nada funcionar, entregue o HTML e oriente: "abra no navegador → Imprimir → Salvar como PDF".

## Encerramento

A resposta termina no aviso legal. Se houve HTML/PDF, uma linha antes dele com os caminhos gerados (`session/relatorio.html`, `.pdf`). Não acrescente "próximos passos", ofertas de aprofundamento nem perguntas (`rules/escrita.md`).
