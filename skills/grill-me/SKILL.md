---
nome: grill-me
descricao: Entrevista obrigatória que transforma o pedido do usuário em um briefing completo e confirmado, antes de qualquer busca.
papel: agents/orquestrador.md
entradas: pedido do usuário (texto, lista de tickers ou extrato colado)
saidas: session/briefing.md com status confirmado
meta: concluir em até 5 minutos
---

# Skill — grill-me

## Regras da entrevista

- **Uma pergunta por mensagem**, sempre com opções numeradas e a opção "outro".
- **Não pergunte o que já foi dito.** Extraia do pedido inicial tudo o que der (tickers, classe, formato, foco) e pergunte só o que falta.
- **Nenhuma busca na web** durante a entrevista. Exceção única: nenhuma.
- Se o usuário disser "tanto faz" / "pula", aplique o **padrão** da tabela e siga.
- Tempo-alvo: ≤ 5 min. Agrupe perguntas só se o usuário pedir ("pode perguntar tudo de uma vez").

## Itens do briefing

| # | Item | Pergunta sugerida | Opções | Padrão se pular |
| --- | --- | --- | --- | --- |
| 1 | Ativos e classe | "Quais ativos estão na carteira?" | lista livre; extrato colado; caminho para CSV | — (obrigatório) |
| 2 | Peso (opcional) | "Quer informar quantidade ou % de cada ativo?" | 1. quantidade 2. % 3. não informar | não informar (consolidada usa pesos iguais e avisa) |
| 3 | Objetivo | "Qual o objetivo principal da carteira?" | 1. renda 2. crescimento 3. preservação | crescimento |
| 4 | Horizonte | "Por quanto tempo pretende manter esses investimentos?" | 1. < 1 ano 2. 1–5 anos 3. > 5 anos | 1–5 anos |
| 5 | Risco | "Como você reage a uma queda de 20% na carteira?" | 1. vendo tudo (baixa) 2. espero (média) 3. vejo como normal (alta) | média |
| 6 | Preocupações | "Tem algum medo ou dúvida específica?" | livre; "nenhuma" | nenhuma |
| 7 | Foco | "O que quer analisar agora?" | 1. carteira toda 2. um ativo 3. uma classe | carteira toda |
| 8 | Formato | "Como quer receber o relatório?" | 1. chat 2. HTML 3. PDF | chat |
| 9 | Detalhe | "Qual nível de detalhe?" | 1. resumido 2. completo | completo |

## Normalização dos ativos

- Converta para ticker oficial em maiúsculas (`petr4` → `PETR4`). Nomes ("Petrobras PN") viram ticker; se ambíguo (ON/PN, units), pergunte.
- Classe pela forma do ticker: final `11` pode ser FII, ETF, unit ou BDR — **pergunte** se não for óbvio. ETFs, BDRs e cripto estão fora do MVP: avise e retire do escopo.
- Tesouro: nome completo do título (`Tesouro IPCA+ 2035`, `Tesouro Selic 2029`, `Tesouro Prefixado 2031`, `Tesouro IPCA+ com Juros Semestrais 2045`, `Tesouro RendA+ 2065`, `Tesouro Educa+ 2040`).
- Extrato/CSV: leia o arquivo indicado, extraia ativos e quantidades e **mostre a lista extraída para confirmação** antes de seguir.

## Encerramento

1. Escreva `session/briefing.md` a partir de [`templates/briefing.md`](../../templates/briefing.md) com `status: rascunho`.
2. Mostre ao usuário um resumo em até 10 linhas e pergunte: "Está correto? (1. sim, pode seguir 2. quero ajustar)".
3. Só com "sim": mude para `status: confirmado` e registre a hora em `confirmado_em`. *(Porta A)*

## Exemplo de abertura

> Vou analisar sua carteira com dados atuais e fontes citadas. Antes, algumas perguntas rápidas (uma por vez).
> Você citou PETR4, ITUB4, HGLG11, MXRF11 e Tesouro IPCA+ 2035. **Qual o objetivo principal da carteira?**
> 1. Renda 2. Crescimento 3. Preservação de patrimônio 4. Outro
