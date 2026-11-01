# Rule — Fontes e dados

> Revisado em: 2026-10-31

## Nenhum número sem fonte

Todo dado factual (cotação, indicador, taxa, evento, data, nome de inquilino, etc.) carrega quatro atributos:

| Atributo | Exemplo |
| --- | --- |
| Valor | `P/VP 0,94` |
| Fonte (URL) | `https://www.fundsexplorer.com.br/funds/hglg11` |
| Data de referência | `2026-09-30` (data a que o dado se refere) |
| Data de coleta | `2026-10-31` (quando você leu a página) |

## Formato de citação

- **Nos arquivos de dados** (`session/dados/*.md`): tabela com as quatro colunas — ver [`templates/dados-coletados.md`](../templates/dados-coletados.md).
- **No relatório:** referência numerada `[n]` logo após o fato, e lista "Fontes" ao final com `[n] Nome da fonte — URL — ref. AAAA-MM-DD — coletado em AAAA-MM-DD`.

## Hierarquia de fontes

1. **Primária oficial:** RI da empresa, CVM (ENET/RAD, fundos.net), B3, Tesouro Nacional, Banco Central.
2. **Agregadores reconhecidos:** Status Invest, Funds Explorer, Fundamentus, Investidor10, Clube FII.
3. **Imprensa especializada:** Valor, InfoMoney, Estadão/E-Investidor, Exame, Brazil Journal — para fatos e contexto, não para indicadores.

Use a fonte de maior nível disponível. A lista concreta e os fallbacks por dado estão em [`knowledge/fontes.md`](../knowledge/fontes.md).

## Defasagem

- Cotação/taxa com mais de **5 dias úteis** de defasagem: sinalize "dado defasado" ao lado do valor.
- Resultado trimestral: use sempre o último divulgado e informe o trimestre (ex.: "2T26").
- Indicadores de FII (vacância, inquilinos): informe o mês do relatório gerencial de origem.

## Conflito entre fontes

Se duas fontes divergem em mais de 5% num mesmo indicador, registre os dois valores com suas fontes, use o da fonte de maior nível e anote a divergência na seção de lacunas.

## Dado não encontrado

Registre `não encontrado` + as fontes tentadas. Nunca preencha com estimativa, memória de treino ou média do setor. O analista trata a lacuna como "dados insuficientes" no critério afetado.
