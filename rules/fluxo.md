# Rule — Fluxo e portas

> Revisado em: 2026-10-31

Uma sessão tem quatro fases — **entrevista, coleta, análise, entrega** — e duas portas obrigatórias.

```
[1 grill-me] → (porta A: usuário confirma briefing) → [2 coleta] → [3 classificação]
→ [4 análise por ativo + consolidada] → [4b aprofundamento] → (porta B: revisor aprova) → [5 entrega]
         ↑ briefing incompleto: volta ao grill-me                     ↑ reprovado: volta ao analista
```

## Portas

- **Porta A — briefing confirmado.** Nenhuma busca na web antes de `session/briefing.md` existir com `status: confirmado`. Se o usuário pular perguntas, registre o padrão assumido e peça confirmação explícita do briefing completo.
- **Porta B — revisão aprovada.** Nenhum relatório é entregue sem `session/revisao.md` com `veredito: APROVADO`. Máximo de **3 ciclos** analista ↔ revisor; no 3º reprovado, entregue apenas as partes aprovadas e liste o que ficou de fora e por quê.

## Proibições

- Não pule etapas, mesmo que o usuário peça "só me diz rápido". Ofereça o detalhe "resumido" no briefing em vez de pular o método.
- Não misture papéis: o revisor não reescreve a análise; o analista não aprova a si mesmo.
- Não entregue relatório parcial sem dizer explicitamente o que falta.
- Não termine a entrega com "próximos passos", ofertas ("posso aprofundar…") ou perguntas. Se um levantamento a mais seria útil, ele acontece no aprofundamento (4b), antes da revisão (`rules/escrita.md`).

## Mudança de escopo no meio da sessão

Se o usuário adicionar/remover ativos ou mudar o foco depois da porta A, atualize `session/briefing.md`, peça nova confirmação e colete só o que falta.
