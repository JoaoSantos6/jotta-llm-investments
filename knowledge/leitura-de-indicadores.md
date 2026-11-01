# Leitura de indicadores — do número à conclusão

> Revisado em: 2026-10-31 · Usado pelo analista ao escrever "Como está hoje", "Saúde financeira" e o cenário econômico · Forma do texto: `rules/escrita.md`

Um número só ganha sentido quando é comparado com uma referência. Todo indicador que vai para o relatório passa por três passos:

1. **Comparar** com uma referência: o próprio histórico do ativo, a mediana do setor ou o índice de mercado.
2. **Classificar** a comparação: `favorável`, `em linha` ou `desfavorável`.
3. **Concluir**: o que isso diz sobre a saúde do ativo ou sobre o risco à frente, em uma frase.

## 1. Referências

### Média do setor

- Use a **mediana de pelo menos 3 pares** do mesmo segmento, da mesma fonte e na mesma data. A mediana é preferível à média porque não é distorcida por um par muito fora da curva.
- Se o agregador publicar o indicador do setor ou segmento, ele pode ser usado no lugar, com fonte.
- Diga sempre **quais pares** formam a referência.
- Com menos de 3 pares comparáveis, use o histórico do próprio ativo e diga que a comparação setorial ficou de fora.

### Faixa "em linha"

- Indicadores em múltiplo ou valor (P/L, P/VP, dívida/EBITDA, cobertura de juros): diferença de até **10%** em relação à referência.
- Indicadores em porcentagem (ROE, margens, DY, vacância): diferença de até **1 p.p.**
- Fora dessas faixas, a comparação é `favorável` ou `desfavorável` conforme a coluna "Melhor quando" das tabelas abaixo.

## 2. Desempenho em três janelas

| Janela | O que mostra | Como ler |
| --- | --- | --- |
| **1 semana** | Reação a eventos recentes (resultado, fato relevante, decisão do Copom) | Quase sempre é ruído. Comente só se o movimento passar de 5% ou tiver um evento identificado; diga que uma semana não define tendência |
| **12 meses** | Tendência recente | Compare com o índice de referência no mesmo período. Ficar muito atrás do índice pede explicação: setor inteiro ou problema da empresa? |
| **5 anos** | Trajetória de longo prazo e consistência | Mostra se o ativo atravessou ciclos econômicos entregando resultado. Desempenho ruim em 5 anos com bom em 12 meses (ou o contrário) merece uma frase sobre o que mudou |

Índices de referência:

| Classe | Índice de mercado | Índice do setor (quando existir) |
| --- | --- | --- |
| Ações | Ibovespa | Índices setoriais da B3: IEE (energia elétrica), IFNC (financeiro), IMAT (materiais básicos), UTIL (utilidade pública), ICON (consumo), IMOB (imobiliário), INDX (industrial), SMLL (small caps) |
| FIIs | IFIX | Mediana dos fundos do mesmo segmento |
| Tesouro Direto | CDI acumulado no período | Taxa do próprio título: hoje × 12 meses atrás × média histórica |
| Carteira | CDI acumulado no período | — |

- Prefira o **retorno total** (com proventos) quando a fonte informar; senão, diga que é só a variação do preço. Isso importa mais em ativos de renda, como FIIs e pagadoras de dividendos.
- Comparar com o CDI responde a pergunta que o investidor faz: "valeu mais que deixar na renda fixa?". Descreva o fato ("rendeu X%, contra Y% do CDI"), sem recomendar.

## 3. Ações

| Indicador | O que mede | Melhor quando | Compare com | Conclusão que ele permite |
| --- | --- | --- | --- | --- |
| ROE | Lucro gerado para cada R$ 100 do capital dos sócios | Maior | Mediana do setor e histórico de 3–5 anos | Se a empresa usa bem o dinheiro dos sócios e se isso está melhorando ou piorando |
| Margem líquida e EBITDA | Quanto sobra de cada R$ 100 vendidos (depois de tudo / da operação) | Maior e estável | Setor e últimos 4 trimestres | Poder de preço e controle de custos; margem caindo com receita subindo indica custo crescendo mais rápido |
| Crescimento do lucro | Evolução do lucro ano contra ano | Maior e consistente | Histórico de 5 anos e setor | Se o negócio está crescendo, estagnado ou encolhendo |
| Dívida líquida/EBITDA | Quantos anos de geração de caixa da operação pagariam a dívida | Menor | Setor (cada setor suporta um nível) | Folga ou aperto financeiro; mais dívida = mais caixa indo para juros e mais sensibilidade à Selic |
| Cobertura de juros | Quantas vezes a geração de caixa da operação paga os juros do período | Maior | Setor | Se a operação paga a dívida com folga ou no limite |
| Fluxo de caixa operacional ÷ lucro | Quanto do lucro vira dinheiro de fato | Perto ou acima de 1 | Histórico | Lucro "de papel" ou lucro que vira caixa |
| Dividend yield (DY) | Proventos dos últimos 12 meses ÷ preço | Maior, **se sustentável** | Setor e histórico | Renda entregue. Sempre leia junto com payout e tendência do lucro: DY alto com lucro caindo ou payout acima de 100% indica renda difícil de repetir |
| Payout | Parte do lucro distribuída | Compatível com o lucro e o investimento necessário | Histórico e setor | Se a distribuição cabe no lucro ou consome caixa e dívida |
| P/L, P/VP, EV/EBITDA | Quanto o mercado paga por real de lucro, de patrimônio ou de geração de caixa | — (não há "melhor") | Mediana do setor e média de 5 anos do ativo | O que o preço embute de expectativa. Ver a seção 6 |

**Bancos e seguradoras:** troque dívida/EBITDA e cobertura de juros por Índice de Basileia (folga de capital; maior = mais folga), inadimplência acima de 90 dias (menor = melhor) e ROE.

**Holdings:** compare o desempenho e os indicadores também com os da principal investida, e diga quanto do valor da holding depende dela.

## 4. FIIs

| Indicador | O que mede | Melhor quando | Compare com | Conclusão que ele permite |
| --- | --- | --- | --- | --- |
| DY | Rendimento dos últimos 12 meses ÷ cota | Maior, **se estável** | Mediana do segmento e CDI/NTN-B | Renda entregue e se ela compensa o risco em relação à renda fixa |
| Rendimento mês a mês | Estabilidade da distribuição | Estável ou crescente | Últimos 12 meses | Se a renda está firme ou foi cortada |
| P/VP | Preço da cota ÷ valor dos ativos do fundo | — (não há "melhor") | Mediana do segmento e histórico | Ver a seção 6 |
| Vacância física e financeira | Área vazia / receita perdida com área vazia | Menor | Mediana do segmento | Área vazia não gera aluguel e gera custo; pressiona o rendimento |
| Maior inquilino (% da receita) | Dependência de um único locatário | Menor | Segmento | Quanto o fundo sofreria se esse inquilino saísse ou atrasasse |
| Prazo médio dos contratos | Quanto tempo a receita está contratada | Maior | Segmento | Previsibilidade da renda |
| Inadimplência / eventos de crédito (papel) | Devedores que atrasaram | Menor | Segmento | Risco de corte de rendimento |
| Alavancagem | Dívida do fundo ÷ patrimônio | Menor | Segmento | Parte da receita comprometida com obrigações |

## 5. Tesouro Direto e macro

**Tesouro.** Compare a taxa atual com a de 12 meses atrás e com a média histórica do título:
- taxa acima da média histórica: quem compra hoje trava um retorno maior que o usual; quem já tem o título viu o preço cair se a taxa subiu desde a compra;
- diga sempre o que acontece se o usuário precisar resgatar antes do vencimento (marcação a mercado) em relação ao horizonte do briefing.

**Macro.** Cada dado do cenário termina dizendo **qual ativo da carteira ele afeta e em que direção** (use as sensibilidades de `knowledge/macro/criterios.md`). Exemplos:
- ❌ "Selic: 13,75% a.a. [9]."
- ✅ "A Selic está em 13,75% ao ano [9] e o mercado espera 11,60% no fim de 2027 [10]. Juros ainda altos encarecem a dívida da Taesa, que é a principal pressão sobre o lucro dela; se o corte esperado vier, essa pressão tende a diminuir."

Dados macro que não afetam nenhum ativo da carteira podem ficar de fora.

## 6. Múltiplos e P/VP: o que o preço embute

Múltiplos não têm "melhor" nem "pior", e o relatório nunca os chama de barato ou caro (`rules/compliance-cvm.md`). A conclusão permitida é **o que o mercado está embutindo no preço** e o que isso implica de risco:

| Situação (com fonte) | Conclusão descritiva |
| --- | --- |
| Múltiplo acima do setor e do histórico | "O mercado paga mais por cada real de lucro do que paga pelos concorrentes. Isso costuma refletir expectativa de crescimento ou de menor risco; se os resultados não acompanharem, o preço tende a ser mais sensível." |
| Múltiplo abaixo do setor, com fundamentos piorando | "O múltiplo baixo vem junto com piora de resultados. Múltiplo baixo, sozinho, não indica saúde do negócio." |
| Múltiplo abaixo do setor, com fundamentos estáveis | "O mercado paga menos por cada real de lucro do que pelos concorrentes. Isso costuma refletir alguma percepção de risco: [citar os riscos do ativo levantados no relatório]." |
| Múltiplo em linha com setor e histórico | "O preço está em linha com o que o mercado paga pelos concorrentes e pelo próprio histórico; o múltiplo não destoa." |
| FII com P/VP acima de 1 | "A cota custa mais que os imóveis/créditos do fundo; o preço depende de o rendimento continuar alto." |
| FII com P/VP abaixo de 1 | "A cota vale menos que os ativos do fundo; isso costuma refletir dúvida do mercado sobre [vacância, crédito, gestão — o que os dados mostrarem]." |

## 7. Saúde financeira — a síntese

Para cada ação, monte a tabela de saúde com quatro pilares e uma frase de conclusão:

| Pilar | Indicadores |
| --- | --- |
| Rentabilidade | ROE e margens vs. setor; tendência |
| Endividamento | Dívida líquida/EBITDA e cobertura de juros vs. setor (bancos: Basileia) |
| Geração de caixa | Fluxo de caixa operacional ÷ lucro |
| Proventos | DY vs. setor, lido junto com payout e tendência do lucro |

A conclusão resume os pilares em linguagem comum: **sólida** (pilares favoráveis ou em linha, nenhum desfavorável), **com pontos de atenção** (um ou dois desfavoráveis) ou **frágil** (três ou mais desfavoráveis, ou endividamento desfavorável junto com caixa desfavorável). Essa síntese descreve a saúde financeira; ela não substitui a situação (🟢🟡🟠🔴) e não é recomendação.

Para FIIs, os pilares são: renda (DY e estabilidade), ocupação ou crédito (vacância ou inadimplência), concentração (maior inquilino ou devedor) e alavancagem.
