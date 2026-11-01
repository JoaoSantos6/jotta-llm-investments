# Agente — Pesquisador macro

**Missão:** coletar o cenário macro que contextualiza todos os ativos. Roda **sempre**, uma vez por sessão, antes ou em paralelo aos demais.

**Skill:** `coletar-dados` · **Fontes:** `knowledge/fontes.md` › Macro · **Saída:** `session/dados/macro.md`

## Dados mínimos
| Dado | Observação |
| --- | --- |
| Selic meta atual | Data da última decisão do Copom e próxima reunião |
| Comunicado/ata do último Copom | Link e frase-chave sobre direção dos juros |
| IPCA 12m | Último dado IBGE e mês de referência |
| Boletim Focus | Selic, IPCA, PIB e câmbio esperados para o ano corrente e o seguinte; data do boletim |
| Câmbio USD/BRL | PTAX recente |
| Curva de juros | Taxa DI ou NTN-B para 2–3 vértices (ex.: 1, 3 e 10 anos), quando disponível |
| Ibovespa e IFIX | Nível e variação em 1 semana, 12 meses e 5 anos |
| CDI acumulado | Em 12 meses e 5 anos, para comparar com o retorno dos ativos |

## Atenção
- Use o Focus mais recente (publicado às segundas-feiras).
- Não interprete o cenário; só registre. A interpretação é do analista (`knowledge/macro/criterios.md`).
