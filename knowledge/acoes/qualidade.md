# Ações — perfil de qualidade do negócio

> Revisado em: 2026-10-31 · Usado por: `skills/classificar-ativo`, `skills/analisar-carteira` · Critérios numéricos: `knowledge/acoes/criterios.md`

Os critérios de `criterios.md` dizem **se há sinal de alerta**. Este arquivo descreve **como é o negócio**: sete dimensões que o analista avalia para cada ação e registra no bloco "Perfil de qualidade" da seção *Estado atual*. Cada dimensão recebe `forte`, `neutra`, `fraca` ou `dados insuficientes`, sempre com o fato e a fonte `[n]` que embasam a marcação.

O perfil é **descritivo**: uma dimensão "forte" não significa que o ativo seja uma boa compra, e "fraca" não significa que deva ser vendido. Nunca some as dimensões em uma nota ou ranking.

## As sete dimensões

| # | Dimensão | Pergunta | Forte | Fraca | Onde encontrar |
| --- | --- | --- | --- | --- | --- |
| Q1 | Histórico de resultados | O lucro é consistente ao longo de vários anos e ciclos? | Lucro positivo em ≥ 8 dos últimos 10 anos (ou em todos os anos disponíveis, se ≥ 5), sem mudança estrutural no negócio | Prejuízo em ≥ 3 dos últimos 5 anos, ou lucro muito errático sem explicação | Agregadores (série histórica de LPA/lucro), DFP |
| Q2 | Rentabilidade vs. pares | O negócio remunera o capital acima dos concorrentes? | ROE e/ou ROIC acima da mediana dos pares listados do mesmo setor nos últimos 3 anos | Abaixo da mediana dos pares de forma persistente | Agregadores; comparar mesmo método de cálculo |
| Q3 | Geração de caixa | O lucro vira caixa? Sobra caixa depois dos investimentos? | Fluxo de caixa operacional ≥ lucro líquido na média de 3 anos e fluxo de caixa livre positivo | Fluxo de caixa operacional persistentemente abaixo do lucro, ou caixa livre negativo sem plano de expansão divulgado | DFC (DFP/ITR), release |
| Q4 | Gestão e alocação de capital | A administração cria valor com o capital que retém? | Ganho de participação de mercado, margens acima dos pares, aquisições/expansões que elevaram a rentabilidade, administradores com participação acionária relevante | Aquisições seguidas de baixas contábeis (impairment), diversificação fora do negócio principal desfeita depois, rotatividade alta na diretoria | Formulário de Referência (histórico, administração), releases, fatos relevantes |
| Q5 | Governança e minoritário | O minoritário é tratado de forma justa? | Conselho com membros independentes, tag along de 100%, histórico sem conflito com minoritários, transações com partes relacionadas pequenas e explicadas | Transações relevantes com o controlador, histórico de disputas com minoritários, troca frequente de controle | Formulário de Referência (controle, administração, partes relacionadas), segmento de listagem na B3 |
| Q6 | Vantagens competitivas | O que impede um concorrente de tomar o mercado? | Ao menos uma vantagem identificável e documentada (ver lista abaixo) | Produto indiferenciado (commodity) sem vantagem de custo, setor com baixa barreira de entrada | Formulário de Referência (atividades), apresentação institucional, imprensa setorial |
| Q7 | Perenidade e ciclicidade | O negócio tende a existir e ser relevante em 10+ anos? Quão sensível é ao ciclo? | Setor perene e pouco cíclico, demanda recorrente, baixo risco de obsolescência | Risco tecnológico/obsolescência evidente, alta dependência de um ciclo de commodity ou de crédito | `knowledge/acoes/setores.md`, fatores de risco do Formulário de Referência |

### Regras de marcação
- **Segmento de listagem não basta.** Novo Mercado ou Nível 2 é um fato positivo de Q5, mas não prova boa governança por si só; registre o segmento e os fatos de conduta separadamente.
- **Bancos e seguradoras:** em Q3, use evolução do patrimônio e do lucro recorrente em vez de fluxo de caixa livre; em Q2, compare ROE apenas com outros bancos/seguradoras.
- **Empresas *asset light*** (varejo com lojas alugadas, serviços, tecnologia): patrimônio contábil baixo infla o ROE e a relação dívida bruta/PL; diga isso ao comentar Q2.
- **Histórico curto** (empresa listada há menos de 5 anos): Q1 = `dados insuficientes` e confiança da classificação no máximo `média`.

## Vantagens competitivas reconhecidas (Q6)

Marca forte · escala/custo mais baixo que os concorrentes · patente ou tecnologia proprietária · concessão ou monopólio regulado · rede de distribuição própria difícil de replicar · integração vertical (controle da matéria-prima) · custo de troca alto para o cliente · efeito de rede · proteção tarifária ou regulatória (registre também como risco, pois pode ser retirada) · acesso a crédito mais barato.

Cite a evidência (participação de mercado, margem superior aos pares, prazo da concessão). Vantagem afirmada só pela própria empresa, sem dado de terceiros, é registrada como "segundo a companhia".

## Concentração de clientes e fornecedores

O Formulário de Referência informa clientes que representam ≥ 10% da receita. Registre sempre. Dependência relevante de um único cliente ou fornecedor é risco específico (ver taxonomia abaixo) e pode disparar AC-12.

## Taxonomia de riscos

Use-a para organizar a seção *Riscos* de cada ação. Comece pelos riscos **específicos** com maior impacto e termine com os **sistêmicos** relevantes para aquele negócio.

**Sistêmicos** (afetam o mercado como um todo; detalhe em `knowledge/macro/criterios.md`): juros, inflação, atividade econômica, câmbio, risco-país, mudanças regulatórias/tributárias amplas, choques externos.

**Específicos** (da empresa e do seu mercado):

| Categoria | Exemplo de evidência |
| --- | --- |
| Concorrencial | Entrada de concorrente, guerra de preços, perda de participação de mercado |
| Obsolescência | Tecnologia substituta, mudança de hábito do consumidor |
| Regulatório | Revisão tarifária, mudança de regra setorial, fim de proteção tarifária |
| Jurídico | Processos relevantes, contingências provisionadas ou não |
| Ambiental | Licenças, passivos ambientais, acidentes |
| Cambial | Receita, custo ou dívida em moeda estrangeira sem proteção |
| Alavancagem | Dívida alta, vencimentos concentrados, indexador da dívida descasado da receita (ex.: dívida em IPCA com receita não indexada) |
| Contratos de receita | Clientes concentrados, contratos curtos ou renegociáveis |
| Fornecedores | Insumo crítico de poucos fornecedores, preço de insumo fora do controle da empresa |
| Conflito de interesses | Transações com controlador ou executivos, remuneração desalinhada |
| Liquidez da ação | Volume baixo dificulta entrada e saída sem afetar o preço |
| Transparência | Divulgação mínima, release sem detalhamento, ausência de teleconferência |

Os fatores de risco que a própria companhia lista no Formulário de Referência são ponto de partida, não teto. Inclua riscos evidentes nos dados mesmo que a empresa não os destaque.

## Small caps

Considere **small cap** a ação com valor de mercado abaixo da mediana das empresas listadas **ou** fora dos índices de maior liquidez (fonte: composição do índice SMLL da B3 e valor de mercado do agregador). Para small caps:

- aplique a régua mais rígida de endividamento (exceção em `criterios.md`);
- registre, quando se aplicarem, os riscos típicos: menor liquidez, maior volatilidade, divulgação mais enxuta, custo de capital mais alto e menor probabilidade de socorro externo em uma crise;
- tamanho não define risco por si só: uma small cap com caixa líquido pode ter risco de negócio menor que uma grande empresa endividada. Descreva o caso concreto.

## Múltiplos: contexto, não veredito

Ao citar P/L, P/VP, EV/EBITDA ou dividend yield, compare com:
1. a **média histórica do próprio ativo** (5 anos, quando a fonte informar);
2. a **mediana dos pares** do mesmo setor.

Escreva os números, a comparação e o que o preço embute, nunca "barato", "caro" ou "descontado". As conclusões permitidas para cada situação estão em `knowledge/leitura-de-indicadores.md` › seção 6. Duas delas, em resumo:
- **Múltiplo alto** (ex.: P/L muito acima do histórico e dos pares): "múltiplos elevados costumam refletir expectativa de crescimento; resultados abaixo dessa expectativa tendem a ter efeito maior sobre o preço".
- **Múltiplo baixo com deterioração** (múltiplo abaixo do histórico **e** algum critério AC-03/04/05/09/10 disparado): "o múltiplo baixo ocorre junto com piora de fundamentos; múltiplo baixo não indica, sozinho, saúde do negócio".
