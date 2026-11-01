# Tesouro Direto — critérios de classificação

> Revisado em: 2026-10-31 · Base: `knowledge/sinais-de-alerta.md`

O risco de crédito do Tesouro é considerado o menor do país; os riscos relevantes para o investidor são **marcação a mercado**, **liquidez/prazo** e **perda de poder de compra** (prefixados).

## Critérios

| ID | Critério | Atenção | Em queda | Perigoso |
| --- | --- | --- | --- | --- |
| TD-01 | Compatibilidade prazo × horizonte | Vencimento até 2 anos além do horizonte do briefing | — | Vencimento > 2 anos além do horizonte **ou** horizonte < 1 ano com título IPCA+/prefixado de vencimento > 5 anos |
| TD-02 | Marcação a mercado 12m | Preço de resgate caiu > 5% em 12m e o horizonte é anterior ao vencimento | Taxa subiu > 1 p.p. em 12m e preço de resgate caiu | — |
| TD-03 | Taxa real vs. histórico (IPCA+) | Taxa real atual abaixo da média histórica disponível do título (registrar como contexto, não como alerta de risco) | — | — |
| TD-04 | Prefixado vs. inflação esperada | Taxa prefixada − IPCA esperado (Focus) < 2 p.p. | — | — |
| TD-05 | Objetivo × indexador | Objetivo "renda" com título sem cupom (o usuário depende de resgate antecipado para renda) | — | — |

## Notas por título

| Título | Comportamento |
| --- | --- |
| Tesouro Selic | Marcação a mercado pequena; adequado a liquidez. TD-02 raramente dispara. |
| Prefixado | Sensível a juros; ganha se juros caem, perde marcação se sobem. Perda real se inflação superar a expectativa. |
| IPCA+ (sem cupom) | Sensibilidade à taxa real cresce com o prazo; vencimentos longos oscilam muito. |
| IPCA+ com juros semestrais | Paga cupons semestrais; reinvestimento e IR a cada cupom. |
| RendA+ / Educa+ | Pagamentos mensais em período definido; resgate antecipado sofre marcação e pode ter regras específicas — verifique na fonte oficial. |

## Saudável

TD-01 não disparado e nenhum outro critério de atenção/queda. Taxa real acima da média (TD-03 invertido) pode ser citada como contexto positivo, com fonte.

## Sempre informar

Que a marcação a mercado só se realiza em caso de resgate antes do vencimento; levando ao vencimento, recebe-se a taxa contratada (descontados IR e custódia).
