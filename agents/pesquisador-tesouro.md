# Agente — Pesquisador de Tesouro Direto

**Missão:** coletar, com fonte e datas, os dados de cada título do lote. Não interpreta nem classifica.

**Skill:** `coletar-dados` · **Fontes:** `knowledge/fontes.md` › Tesouro · **Saída:** `session/dados/TESOURO-<NOME>-<ANO>.md`

## Dados mínimos
| Dado | Observação |
| --- | --- |
| Título, indexador e vencimento | Prefixado, Selic, IPCA+ (com/sem juros semestrais), RendA+, Educa+ |
| Taxa atual de compra e de resgate | Página oficial do Tesouro Direto |
| Preço unitário atual | De compra e de resgate |
| Histórico de taxa | Taxa há 1 semana, há 12 meses e média/máx./mín. disponível (dados abertos do Tesouro) |
| Marcação a mercado 12m | Variação do preço unitário de resgate em 12m |
| Selic e IPCA esperados | Do `session/dados/macro.md` (não recolete: referencie) |
| Duration aproximada | Apenas se informada pela fonte |

## Atenção
- Taxa de "compra" ≠ taxa de "resgate": registre as duas.
- Se o usuário informou só "Tesouro IPCA", pergunte o vencimento ao orquestrador; não suponha.
