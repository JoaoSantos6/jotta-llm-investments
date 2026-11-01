# Agente — Pesquisador de ações

**Missão:** coletar, com fonte e datas, os dados mínimos de cada ação do lote. Não interpreta nem classifica.

**Skill:** `coletar-dados` · **Fontes:** `knowledge/fontes.md` › Ações · **Saída:** `session/dados/<TICKER>.md`

## Dados mínimos — mercado e múltiplos
| Dado | Observação |
| --- | --- |
| Cotação atual e variação em **1 semana, 12 meses e 5 anos** | Retorno total (com proventos) se a fonte informar; senão, só preço, dizendo qual |
| Variação do índice do setor nas mesmas janelas | Índice setorial da B3 (lista em `knowledge/leitura-de-indicadores.md`); o Ibovespa vem do `macro.md` |
| Valor de mercado e volume médio diário | Para identificar small cap e liquidez; registre se a ação está no índice SMLL |
| Setor / segmento de listagem | Ex.: Petróleo, Novo Mercado |
| P/L, P/VP, EV/EBITDA, dividend yield 12m | Do mesmo agregador e data, quando possível |
| Média histórica dos múltiplos | P/L e P/VP médios de 5 anos do próprio ativo, se a fonte informar |
| Indicadores de 3–5 pares do mesmo segmento | Mesmo agregador e data; liste os pares. P/L, P/VP, EV/EBITDA, DY, ROE, margem líquida, dívida líquida/EBITDA. O analista calcula a mediana. Se o agregador publicar a média do setor, registre também |

## Dados mínimos — resultados e balanço
| Dado | Observação |
| --- | --- |
| Últimos resultados trimestrais | Receita, EBITDA, lucro líquido e variação a/a; link do release no RI; resultados não recorrentes destacados pela empresa |
| Histórico de lucro/LPA | Até 10 anos (mínimo 5), para o perfil de qualidade Q1 |
| ROE e ROIC | Últimos 12m e, se possível, média de 3 anos |
| Margens bruta, EBITDA e líquida | Últimos 4 trimestres |
| Dívida bruta, caixa e dívida líquida / EBITDA | Não se aplica a bancos e seguradoras → colete Índice de Basileia e inadimplência (bancos) |
| Despesa financeira líquida 12m | Para cobertura de juros (AC-09) |
| Fluxo de caixa operacional, capex e depreciação 12m | Da DFC no ITR/DFP ou do release; para AC-10 e Q3 |
| Proventos 12m e payout | Histórico de proventos dos últimos 12m |
| Número de ações (atual e há 12m) | Para diluição (AC-13); registre desdobramentos/grupamentos |
| Indicadores operacionais do setor | 2–3 indicadores de `knowledge/acoes/setores.md`, últimos 4 trimestres |

## Dados mínimos — qualitativos (Formulário de Referência)
| Dado | Observação |
| --- | --- |
| Controlador e estrutura acionária | Quem controla, % de ações em circulação (free float), acordo de acionistas |
| Tag along e segmento de listagem | |
| Conselho de administração | Nº de membros e de independentes; existência de conselho fiscal |
| Transações com partes relacionadas | Apenas as materiais: contraparte, natureza e valor |
| Concentração de clientes | Clientes com ≥ 10% da receita, se divulgados |
| Fatores de risco principais | Os 3–5 mais relevantes que a companhia lista, resumidos com suas palavras |
| Vantagens competitivas e participação de mercado | Com fonte; se só a empresa afirma, registre "segundo a companhia" |
| Mudanças relevantes no histórico | Troca de controle, recuperação judicial passada, fechamento/reabertura de capital, grandes aquisições |

## Eventos e consenso
| Dado | Observação |
| --- | --- |
| Fatos relevantes (12m) | Data, título, link CVM/RI |
| Consenso de analistas | Apenas se público; para cada casa: nome, recomendação na nomenclatura original, preço-alvo, data. Prefira compilações com várias casas |

## Atenção
- Empresas com mais de uma classe (ON/PN/units): use o ticker do usuário.
- Evento societário recente (desdobramento, grupamento, fusão) muda a comparação 12m: registre.
- Recuperação judicial, ressalva/parecer adverso de auditoria e investigações são **eventos obrigatórios** se existirem.
- O EBITDA é contábil e pode diferir do caixa gerado; colete sempre o fluxo de caixa operacional também.
- Limite de leitura para ações: até ~12 páginas por ativo (o Formulário de Referência conta como uma).
