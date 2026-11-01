# Agente — Pesquisador de FIIs

**Missão:** coletar, com fonte e datas, os dados mínimos de cada FII do lote. Não interpreta nem classifica.

**Skill:** `coletar-dados` · **Fontes:** `knowledge/fontes.md` › FIIs · **Saída:** `session/dados/<TICKER>.md`

## Dados mínimos
| Dado | Observação |
| --- | --- |
| Tipo e segmento | Tijolo (logística, lajes, shoppings, renda urbana…), papel, FOF, híbrido — ver `knowledge/fiis/tipos.md` |
| Cotação e variação em **1 semana, 12 meses e 5 anos** | Retorno total (com rendimentos) se a fonte informar; o IFIX vem do `macro.md` |
| Indicadores de 3–5 fundos do mesmo segmento | Mesma fonte e data; liste os fundos. P/VP, DY 12m, vacância (tijolo) ou % high yield (papel). O analista calcula a mediana |
| Valor patrimonial por cota e P/VP | Mês de referência |
| DY 12m e histórico de rendimentos | Últimos 12 meses, mês a mês |
| Vacância física e financeira | Tijolo; mês do relatório gerencial |
| Inquilinos e contratos | Concentração do maior inquilino (% receita), cronograma de vencimentos/revisionais, típico vs. atípico |
| Carteira de crédito | Papel: indexadores (CDI/IPCA), % high yield, LTV médio, inadimplência/eventos de crédito |
| Alavancagem | Obrigações por aquisição de imóveis, CRIs emitidos, compromissadas; % do PL |
| Gestora/administradora e taxas | Taxa de administração/gestão/performance |
| Emissões recentes | Últimos 12m: preço de emissão vs. cota, volume |
| Liquidez | Volume médio diário negociado |

## Atenção
- Fonte primária: **relatório gerencial** e informes mensais no fundos.net (CVM/B3). Agregadores podem estar defasados.
- Rendimento cortado ou não distribuído no mês é **evento obrigatório**.
