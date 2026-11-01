# Teste 01 — Carteira mista completa (caso de uso 1)

## Entrada

> Tenho PETR4, ITUB4, HGLG11, MXRF11 e Tesouro IPCA+ 2035. Analise minha carteira.

**Respostas do usuário ao grill-me:** pesos iguais (não informar) · objetivo renda · horizonte > 5 anos · tolerância média · preocupação "medo de corte de dividendos" · carteira toda · chat · completo.

## Comportamento esperado

- [ ] Não faz nenhuma busca antes de confirmar o briefing.
- [ ] Não pergunta de novo os ativos já citados; pergunta uma coisa por vez, com opções.
- [ ] Mostra resumo do briefing e pede confirmação; grava `session/briefing.md` com `status: confirmado`.
- [ ] Coleta macro + ações + FIIs + Tesouro (em paralelo se suportar subagentes).
- [ ] `session/dados/` tem 5 arquivos de ativo + `macro.md`, todos com valor, URL, data de referência e data de coleta.
- [ ] ITUB4 usa a exceção de bancos (Basileia, sem dívida líq./EBITDA).
- [ ] MXRF11 é tratado como FII de papel (critérios FP-*, sem vacância).
- [ ] Tesouro IPCA+ 2035 é avaliado quanto a marcação a mercado e compatibilidade com horizonte > 5 anos.
- [ ] Cada ativo tem as 7 seções; a preocupação "corte de dividendos" é respondida para PETR4, ITUB4, HGLG11 e MXRF11.
- [ ] Consolidada avisa que usa pesos iguais e não dispara concentração por peso.
- [ ] `session/revisao.md` existe com `veredito: APROVADO`.
- [ ] Entrega em chat com alertas no topo, tabela-síntese, fontes e disclaimer.

## Reprova se

- Qualquer número sem fonte `[n]` no relatório.
- Qualquer termo proibido de `rules/compliance-cvm.md` ("compre", "venda", "oportunidade", "preço justo"…).
- Ausência do disclaimer.
- Relatório entregue sem revisão aprovada.
