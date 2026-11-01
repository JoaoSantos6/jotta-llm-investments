# Ações — critérios de classificação

> Revisado em: 2026-10-31 · Base: `knowledge/sinais-de-alerta.md` · Setores: `knowledge/acoes/setores.md` · Perfil de qualidade: `knowledge/acoes/qualidade.md`

## Critérios

| ID | Critério | Atenção | Em queda | Perigoso |
| --- | --- | --- | --- | --- |
| AC-01 | Variação 12m | — | Queda > 20% **e** pior que o Ibovespa em > 10 p.p. | — |
| AC-02 | Dívida líquida / EBITDA | > 3,0x ou subiu > 1,0x em 12m | — | > 4,0x **com** fluxo de caixa livre negativo nos últimos 12m |
| AC-03 | Margem EBITDA / líquida | Queda > 5 p.p. em relação ao mesmo período do ano anterior | — | Prejuízo líquido em 3 dos últimos 4 trimestres |
| AC-04 | Lucro líquido | Queda > 30% a/a no último trimestre | Queda > 30% a/a em 2 trimestres seguidos | — |
| AC-05 | ROE | < 8% ou queda > 5 p.p. em 12m | — | Negativo nos últimos 12m |
| AC-06 | Proventos | Corte > 30% nos proventos 12m sem motivo extraordinário divulgado | — | Suspensão de proventos por restrição de caixa/covenant |
| AC-07 | Governança e eventos | Fato relevante negativo material (multa, perda de contrato, revisão de guidance para baixo) | — | Recuperação judicial/extrajudicial, ressalva de auditoria, fraude/investigação |
| AC-08 | Ciclo setorial | Setor cíclico com indicador do ciclo virando (ver `setores.md`) | — | — |
| AC-09 | Cobertura de juros (EBITDA 12m ÷ despesa financeira líquida 12m) | < 2,0x | — | < 1,0x (a operação não cobre os juros) |
| AC-10 | Qualidade do lucro (fluxo de caixa operacional 12m ÷ lucro líquido 12m) | < 0,5 em 2 anos seguidos, sem explicação divulgada (ex.: expansão de capital de giro planejada) | — | — |
| AC-11 | Coerência lucro × proventos | Proventos 12m > lucro líquido 12m (payout > 100%) sem reserva/caixa que explique | — | Proventos distribuídos com prejuízo no período **e** dívida líquida crescendo |
| AC-12 | Concentração de clientes | Um único cliente > 25% da receita | — | Cliente > 25% da receita em recuperação judicial, inadimplente ou rescindindo contrato |
| AC-13 | Diluição | Número de ações cresceu > 10% em 12m (emissão, conversão, planos de opções) | — | — |
| AC-14 | Partes relacionadas | Transações com controlador/administradores materiais (> 5% da receita ou do custo) ou sem condições de mercado demonstradas | — | — |

### Como medir

- **AC-09:** use a despesa financeira líquida (despesas − receitas financeiras) dos últimos 12 meses. Se a empresa tiver receita financeira líquida (caixa maior que a dívida), o critério não dispara — registre "caixa líquido". Variação cambial e ganhos/perdas com derivativos entram somente se a fonte não os separar; diga qual base usou.
- **AC-10 / AC-11:** use 12 meses acumulados para neutralizar sazonalidade. Resultados não recorrentes (venda de ativos, créditos tributários, baixas contábeis) divulgados no release devem ser identificados e, quando a empresa informar o lucro ajustado, cite os dois.
- **ROE (AC-05):** lucro líquido dos últimos 12 meses sobre o patrimônio líquido. Ao comparar empresas, use a mesma fonte e o mesmo método para todas.
- **Dívida bruta/PL alta com dívida líquida negativa** (caixa maior que a dívida) não é sinal de alerta: registre como fato e não dispare AC-02.
- **Lucro sem proventos** por vários anos não dispara critério, mas registre se a empresa não divulga destino do lucro retido (investimentos, aquisições, redução de dívida).

## Exceções por setor

| Setor | Exceção |
| --- | --- |
| Small caps (ver `qualidade.md`) | Régua mais rígida de balanço: AC-02 dispara atenção acima de 2,0x e perigoso acima de 3,0x com fluxo de caixa livre negativo; AC-09 dispara atenção abaixo de 3,0x. |
| Bancos | Não usar AC-02, AC-09, AC-10 nem margem EBITDA. Usar: Índice de Basileia < 12% → atenção; < 11% → perigoso; inadimplência > 90 dias subindo > 1 p.p. em 12m → atenção. ROE (AC-05) é central. |
| Seguradoras | Não usar AC-02, AC-09 nem AC-10. Usar índice combinado > 100% → atenção. |
| Elétricas transmissoras / saneamento (receita regulada) | AC-02: atenção só acima de 4,0x; perigoso acima de 5,0x com caixa negativo. AC-09: atenção abaixo de 1,5x. |
| Setores intensivos em capital (mineração, siderurgia, papel e celulose, petróleo, petroquímica) | Dívida bruta/PL alta é típica do setor; use AC-02 e AC-09, não a dívida bruta/PL, para julgar o endividamento. |
| Holdings | Usar dívida líquida da holding (individual), se divulgada; senão marcar dados insuficientes. |
| Empresas em fase pré-operacional / crescimento com prejuízo | AC-03/AC-05 marcados como "não aplicável" se o prejuízo é esperado e divulgado; diga isso. |

## Em queda: ruído ou estrutural?

| Evidência | Aponta para |
| --- | --- |
| Setor e Ibovespa caíram de forma parecida; lucro/caixa estáveis | Ruído de mercado |
| Queda após fato relevante específico, revisão de guidance, perda de contrato | Estrutural |
| Lucro, margem ou ROE pioraram (AC-03/04/05 disparados) | Estrutural |
| Queda concentrada após data-com de provento extraordinário relevante | Ruído (efeito ex-dividendo) |
| Mudança regulatória/tributária que afeta o setor | Estrutural setorial |
| Queda após emissão de ações com desconto (AC-13) | Diluição (estrutural de curto prazo) |
| Desdobramento ou grupamento no período | Nenhuma — o preço nominal muda sem alterar o valor da empresa; ajuste a comparação 12m antes de avaliar AC-01 |

## Risco sistêmico × específico

Ao classificar a causa de uma queda, diga também se o fator dominante é **sistêmico** (juros, câmbio, atividade, risco-país — afeta o mercado todo) ou **específico** (da empresa ou do seu mercado). A taxonomia completa está em `knowledge/acoes/qualidade.md`.

## Saudável

Nenhum critério disparado **e** ao menos 9 dos 14 critérios com dados suficientes.
