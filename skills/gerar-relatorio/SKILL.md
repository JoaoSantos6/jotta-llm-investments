---
nome: gerar-relatorio
descricao: Renderiza o relatório aprovado no formato pedido (chat, HTML autocontido ou PDF) e entrega só o que foi pedido.
papel: agents/orquestrador.md
entradas: session/relatorio.md (aprovado), session/briefing.md
saidas: resposta no chat (formato chat) ou arquivo(s) session/relatorio-AAAA-MM-DD-HHMM-ATIVOS.html e/ou .pdf (formatos HTML/PDF)
---

# Skill — Gerar relatório

**Pré-condição:** `session/revisao.md` com `veredito: APROVADO`. Os renderizadores **não alteram conteúdo** — só formato. Nenhum fato novo entra nesta etapa.

## O que o chat recebe: só o que foi pedido

| Formato pedido | O chat traz |
| --- | --- |
| Chat | O relatório no formato chat (seção abaixo) e o aviso legal no fim. |
| HTML | **Somente o arquivo HTML** e o aviso legal. |
| PDF | **Somente o arquivo PDF** e o aviso legal. |
| HTML e PDF | **Somente os dois arquivos** e o aviso legal. |

Quando o formato é HTML ou PDF, o chat **não repete o conteúdo**: nada de resumo, leitura rápida, tabela, lista de alertas, explicação de como o arquivo funciona nem caminho em texto corrido. O arquivo é entregue pelo meio que a ferramenta oferece (anexo, cartão de arquivo); só se não houver como anexar, o caminho do arquivo vai sozinho, numa linha. Depois do(s) arquivo(s), vem o aviso legal de [`templates/disclaimer.md`](../../templates/disclaimer.md), sem alterações. Nada mais.

## Nome dos arquivos

O nome diferencia um relatório do outro: carrega a data e a hora da geração e os ativos analisados.

```
session/relatorio-AAAA-MM-DD-HHMM-TICKER1-TICKER2.html
session/relatorio-AAAA-MM-DD-HHMM-TICKER1-TICKER2.pdf
```

- **Data e hora:** do momento da geração, no fuso do usuário se for conhecido; senão, o do sistema. Formato `AAAA-MM-DD-HHMM` (ex.: `2026-11-02-0932`).
- **Ativos:** tickers em maiúsculas, na ordem do briefing, separados por hífen (`TAEE4-VIVT3`). Tesouro entra com o nome sem espaços nem `+` (`TESOURO-IPCA-2035`, como em `session/dados/`).
- **Mais de 4 ativos:** os 3 primeiros e `mais-N` (ex.: `PETR4-ITUB4-HGLG11-mais-3`).
- O PDF leva o mesmo nome-base do HTML de onde saiu. Gerar de novo no mesmo minuto sobrescreve o arquivo; em outro minuto, cria um arquivo novo e não apaga os anteriores.

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

Esta seção vale **só quando o formato pedido é chat**. Para HTML e PDF, o chat não recebe versão alguma do conteúdo (ver "O que o chat recebe").

## HTML

1. Copie [`templates/relatorio.html`](../../templates/relatorio.html) para `session/relatorio-AAAA-MM-DD-HHMM-ATIVOS.html` (ver "Nome dos arquivos").
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
1. **Script:** `python scripts/gerar_pdf.py session/relatorio-AAAA-MM-DD-HHMM-ATIVOS.html` (usa Chrome/Edge/Chromium headless já instalado; sem dependências Python).
2. **Ferramenta nativa** da LLM, se houver (ex.: geração de PDF embutida), a partir do mesmo HTML.
3. **Manual:** se nada funcionar, entregue o HTML e diga numa frase que o PDF não pôde ser gerado e como obtê-lo ("abra no navegador → Imprimir → Salvar como PDF"). É a única exceção à regra de "só o arquivo e o aviso legal".

## Encerramento

A resposta termina no aviso legal. Em HTML/PDF, a resposta é só o(s) arquivo(s) e o aviso legal, sem linha de apresentação, sem caminhos em texto e sem comentários. Não acrescente "próximos passos", ofertas de aprofundamento nem perguntas (`rules/escrita.md`).
