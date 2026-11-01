# Carteira — critérios da análise consolidada

> Revisado em: 2026-10-31

Limiares de referência do framework para descrever concentração e exposição. Disparar um limiar gera **alerta descritivo**, nunca sugestão de alocação.

## Concentração

| ID | Critério | Alerta quando |
| --- | --- | --- |
| CA-01 | Peso de um único ativo | > 20% da carteira |
| CA-02 | Peso de um setor/segmento (ações + FIIs do mesmo segmento) | > 35% |
| CA-03 | Peso de uma classe | > 70% (exceto Tesouro Selic) |
| CA-04 | Ativos classificados como 🔴 perigoso | Soma > 10% da carteira |
| CA-05 | Ativos 🟠/🔴 | Soma > 25% da carteira |
| CA-06 | Número de ativos de risco variável (ações + FIIs) | < 5 (baixa diversificação) |

Sem pesos informados: use pesos iguais, **diga que são iguais por falta de informação** e não dispare CA-01/02/03 com base neles (apenas CA-06).

Cálculo de pesos com quantidades: `peso = quantidade × cotação coletada / total`. Mostre a cotação usada com fonte. Para Tesouro, use o preço unitário de resgate.

## Exposição macro

Para cada fator (juros, inflação, câmbio), liste os ativos sensíveis e a direção típica usando `knowledge/macro/criterios.md` e `knowledge/fiis/tipos.md`. Diga a soma de pesos expostos na mesma direção. Exposição > 50% da carteira na mesma direção de um fator → alerta CA-07.

## Correlações óbvias

Sinalize quando 2+ ativos compartilham o mesmo risco: mesmo setor, mesmo inquilino/devedor relevante, mesmo grupo econômico, mesmo indexador.

## Compatibilidade com o briefing (descritiva)

| Briefing | Pergunta a responder no relatório |
| --- | --- |
| Objetivo renda | Qual parcela da carteira distribui renda periódica (FIIs, ações com DY, títulos com cupom)? |
| Objetivo preservação | Qual parcela está em ativos com marcação/volatilidade relevante? |
| Horizonte < 1 ano | Algum ativo tem prazo ou volatilidade incompatível (ver TD-01)? |
| Tolerância baixa | Qual parcela está em ativos 🟠/🔴 ou em queda > 20% em 12m? |

## Priorização de alertas (máx. 5)

1. Ativos 🔴 (maior peso primeiro).
2. CA-04/CA-05.
3. Incompatibilidades com o briefing.
4. Concentrações (CA-01/02/03/07).
5. Ativos 🟠 e 🟡 (maior peso primeiro).
