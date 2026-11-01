---
nome: orquestrar-sessao
descricao: Conduz uma sessão de análise de carteira do início ao fim, chamando as demais skills na ordem e respeitando as portas.
papel: agents/orquestrador.md
entradas: pedido do usuário
saidas: session/ completo e relatório entregue
---

# Skill — Orquestrar sessão

## Passo a passo

1. **Preparar.** Carregue as rules (ver `AGENTS.md`). Se `session/` já tiver conteúdo, aplique `rules/privacidade.md` (arquivar ou apagar). Crie `session/`, `session/dados/` e `session/analise/`.
2. **Entrevista.** Execute [`skills/grill-me`](../grill-me/SKILL.md) até `session/briefing.md` ter `status: confirmado`. *(Porta A)*
3. **Plano de coleta.** A partir do briefing, monte a lista de trabalho:
   - sempre: `macro` (pesquisador-macro);
   - um item por classe presente no foco: `acoes`, `fiis`, `tesouro`;
   - lotes de **até 5 ativos** por classe.
   Grave o plano no topo de `session/log.md`.
4. **Coleta.** Execute [`skills/coletar-dados`](../coletar-dados/SKILL.md):
   - com subagentes: dispare macro + um subagente por lote **em paralelo**;
   - sem subagentes: macro primeiro, depois cada lote em sequência.
5. **Checagem de cobertura.** Para cada ativo, confira se `session/dados/<ATIVO>.md` existe e se os dados mínimos da classe foram coletados ou marcados `não encontrado`. Se faltar arquivo, rode a coleta de novo só para ele (1 nova tentativa).
6. **Classificação e análise.** Execute [`skills/classificar-ativo`](../classificar-ativo/SKILL.md) e depois [`skills/analisar-carteira`](../analisar-carteira/SKILL.md).
7. **Aprofundamento.** Leia a seção `## Perguntas em aberto` de cada `session/analise/<ATIVO>.md` e de `consolidada.md`. São dúvidas que um levantamento a mais resolveria e que mudariam a leitura do usuário (ex.: causa de uma queda forte, um dado que pode mudar a situação do ativo, um fato relevante citado sem detalhe). Para cada uma, dentro do escopo e do compliance:
   - rode uma **coleta pontual** com o pesquisador da classe (mesmas regras de `skills/coletar-dados`), gravando em `session/dados/<ATIVO>.md`;
   - devolva ao analista para atualizar classificação e análise.
   Faça **uma rodada**, com até 2 perguntas por ativo. O que continuar sem resposta vai para "O que esta análise não cobriu". Registre no `session/log.md`.
8. **Revisão.** Execute [`skills/revisar-relatorio`](../revisar-relatorio/SKILL.md). Se `REPROVADO`, devolva os apontamentos ao analista e repita 6→8 (máx. 3 ciclos, ver `rules/fluxo.md`). Nova coleta pontual pedida pelo revisor conta como aprofundamento. *(Porta B)*
9. **Entrega.** Execute [`skills/gerar-relatorio`](../gerar-relatorio/SKILL.md) no formato do briefing. A entrega termina no aviso legal: sem "próximos passos", sem ofertas e sem perguntas ao usuário (`rules/escrita.md`).

## Comunicação com o usuário durante a sessão

- Ao iniciar cada fase, uma linha de status: "Coletando dados de 3 FIIs e 2 ações…".
- Não despeje dados brutos no chat; eles ficam em `session/dados/`.
- Linhas de status são curtas e não usam códigos internos nem nomes de etapas do framework ("Buscando a causa da queda de ITSA4…", não "Executando passo 7 / AC-01").
- Se uma fonte bloquear, siga o fallback de `knowledge/fontes.md` sem interromper o usuário.

## `session/log.md`

Registro cronológico curto: plano de coleta, subagentes disparados, fontes bloqueadas, ciclos de revisão e veredito. Uma linha por evento, com hora.
