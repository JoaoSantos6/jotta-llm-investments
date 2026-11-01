# Fontes oficiais do MVP e fallbacks

> Revisado em: 2026-10-31 · Hierarquia e formato de citação: `rules/fontes-e-dados.md`

Para cada dado, tente as fontes **na ordem**. Se uma bloquear leitura automática (captcha, 403, conteúdo só via JavaScript), passe à seguinte e registre o bloqueio em `session/log.md`. Os padrões de URL são pontos de partida; se mudarem, busque "<ticker> <fonte>".

## Ações

| Dado | 1ª fonte | Fallback (em ordem) |
| --- | --- | --- |
| Cotação, variação 1 semana / 12 meses / 5 anos | Status Invest `statusinvest.com.br/acoes/<ticker>` | Investidor10 `investidor10.com.br/acoes/<ticker>/` · Fundamentus `fundamentus.com.br/detalhes.php?papel=<TICKER>` · B3 |
| P/L, P/VP, ROE, margens, Dív.líq/EBITDA, DY | Status Invest | Investidor10 · Fundamentus |
| Resultados trimestrais | Site de RI da empresa (release/ITR) | CVM RAD `rad.cvm.gov.br` · Status Invest |
| Fluxo de caixa (operacional, capex), despesa financeira | ITR/DFP — Demonstração dos Fluxos de Caixa e notas explicativas (RI ou CVM RAD) | Release de resultados · Status Invest |
| Histórico de lucro/LPA, ROE, ROIC, múltiplos históricos | Status Invest | Investidor10 · Fundamentus |
| Controle, administração, partes relacionadas, clientes, fatores de risco, histórico | **Formulário de Referência** (CVM RAD ou site de RI) | Apresentação institucional (menos completa; tende a destacar só o positivo) |
| Indicadores dos pares do setor (para a mediana) | Status Invest (páginas dos pares e do setor) | Investidor10 · Fundamentus |
| Índices setoriais (IEE, IFNC, IMAT, UTIL, ICON, IMOB, INDX) | B3 | Investing.com · imprensa |
| Segmento de listagem, tag along, índices (SMLL, IGC) | B3 (página da empresa listada e composição dos índices) | Site de RI · Status Invest |
| Fatos relevantes | CVM RAD | Site de RI · B3 (Plantão de Notícias) |
| Proventos | Site de RI | Status Invest · Investidor10 |
| Consenso de analistas | Matérias de imprensa que compilam recomendações de várias casas (Valor, InfoMoney, E-Investidor) | Investidor10 (quando houver) |
| Contexto/notícias | Valor Econômico · InfoMoney · Brazil Journal | Exame · Estadão/E-Investidor |

### Documentos obrigatórios das companhias abertas

| Documento | O que traz | Periodicidade |
| --- | --- | --- |
| DFP (demonstrações financeiras anuais) | Balanço, resultado, fluxo de caixa, valor adicionado, notas explicativas, parecer do auditor | Anual |
| ITR (informações trimestrais) | Demonstrações do trimestre, com revisão do auditor | Trimestral (1º a 3º trimestre) |
| Formulário de Referência | Histórico, atividades, mercado, clientes, concorrentes, controle, administração, remuneração, partes relacionadas, fatores de risco | Anual, atualizado quando há mudança relevante |
| Release de resultados | Resumo gerencial do trimestre, indicadores operacionais, ajustes não recorrentes | Trimestral (não obrigatório, mas usual) |

Dados contábeis vêm dos documentos auditados (DFP/ITR); o release serve para indicadores operacionais e ajustes, sempre identificados como "segundo a companhia".

### Consenso de analistas

- Prefira compilações que reúnam **várias casas**; cite a quantidade de casas e a data.
- As casas usam nomenclaturas diferentes para a mesma ideia (ex.: compra / outperform / overweight; neutro / manter / market weight; venda / underperform / underweight). Ao resumir, agrupe em três faixas — **positiva, neutra, negativa** — e mantenha o termo original entre parênteses.
- Relatórios de casas de análise trazem aviso de conflitos de interesse; se a fonte indicar relação comercial da casa com a empresa, registre.

## FIIs

| Dado | 1ª fonte | Fallback (em ordem) |
| --- | --- | --- |
| Relatório gerencial, informe mensal | fundos.net B3/CVM `fnet.bmfbovespa.com.br` | Site da gestora · Funds Explorer |
| Cotação, P/VP, DY, rendimentos | Funds Explorer `fundsexplorer.com.br/funds/<ticker>` | Status Invest `statusinvest.com.br/fundos-imobiliarios/<ticker>` · Investidor10 `investidor10.com.br/fiis/<ticker>/` · Clube FII |
| Vacância, inquilinos, contratos | Relatório gerencial | Funds Explorer · Clube FII |
| Carteira de CRIs (papel) | Relatório gerencial / informe mensal | Site da gestora |
| Emissões | fundos.net (fatos relevantes/comunicados) | Funds Explorer |
| IFIX | B3 | Status Invest · Investidor10 |
| Indicadores dos fundos do mesmo segmento | Funds Explorer (ranking por segmento) | Status Invest · Clube FII |

## Tesouro Direto

| Dado | 1ª fonte | Fallback (em ordem) |
| --- | --- | --- |
| Taxas e preços atuais | Tesouro Direto `tesourodireto.com.br` (Preços e taxas) | Tesouro Transparente (dados abertos) · Status Invest (títulos públicos) |
| Histórico de taxas/preços | Tesouro Transparente `tesourotransparente.gov.br` (dataset "Taxas dos Títulos Ofertados pelo Tesouro Direto") | Investidor10 · Status Invest |

## Macro

| Dado | 1ª fonte | Fallback (em ordem) |
| --- | --- | --- |
| Selic meta, Copom | Banco Central `bcb.gov.br` (Copom: comunicados e atas) | Imprensa (Valor, InfoMoney) |
| Boletim Focus | Banco Central `bcb.gov.br/publicacoes/focus` | Imprensa que reporta o boletim do dia |
| IPCA | IBGE `ibge.gov.br` | Banco Central (SGS série 13522) · imprensa |
| Câmbio (PTAX) | Banco Central | Imprensa |
| Curva de juros | ANBIMA (curvas de juros/ETTJ) | Tesouro Direto (taxas de NTN-B como proxy, informando que é proxy) · imprensa |
| Ibovespa | B3 | Status Invest · Investidor10 |
| CDI acumulado | B3 / Banco Central (SGS série 12) | Calculadoras de rentabilidade de corretoras e imprensa |

## Extensões opcionais (fora do MVP)

Documentadas para quem quiser integrar APIs. Não exigidas pelo fluxo.

- **API SGS do Banco Central** (gratuita, sem chave): `https://api.bcb.gov.br/dados/serie/bcdata.sgs.<codigo>/dados/ultimos/1?formato=json` — 432 (Selic meta), 13522 (IPCA 12m), 1 (dólar comercial).
- **brapi** `brapi.dev` — cotações e fundamentos de ações e FIIs (plano gratuito com limites; exige token).
- **Dados abertos do Tesouro Transparente** — CSV de taxas e preços históricos.
- **Dados abertos CVM** `dados.cvm.gov.br` — demonstrações financeiras e informes de FII.
