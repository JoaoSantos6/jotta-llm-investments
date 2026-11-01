# Teste 02 — Foco em uma classe: FIIs (caso de uso 2)

## Entrada

> Analise só meus FIIs com foco em risco de vacância e dividendos: HGLG11 (200 cotas), KNRI11 (150), XPML11 (100), KNCR11 (300). Também tenho PETR4, mas não precisa olhar.

**Respostas do usuário ao grill-me:** objetivo renda · horizonte 1–5 anos · tolerância baixa · formato HTML · detalhe completo.

## Comportamento esperado

- [ ] Extrai do pedido: foco `classe:fiis`, quantidades e a preocupação (vacância e dividendos) — não pergunta de novo.
- [ ] PETR4 fica fora do foco e não é coletado.
- [ ] Classifica corretamente os tipos: HGLG11 tijolo/logística, KNRI11 tijolo/híbrido lajes+logística, XPML11 tijolo/shoppings, KNCR11 papel CDI.
- [ ] Vacância física e financeira coletadas para os de tijolo (ou `não encontrado` com fontes tentadas); KNCR11 sem critério de vacância.
- [ ] Pesos calculados por quantidade × cotação coletada, com a cotação citada.
- [ ] Consolidada aborda concentração por segmento e exposição a juros (tijolo vs. papel CDI em direções opostas).
- [ ] Gera `session/relatorio.html` autocontido, sem `{{` remanescente, e um resumo no chat.

## Reprova se

- Coleta dados de PETR4.
- Aplica critério de vacância ao KNCR11.
- HTML carrega CSS/JS externo ou ficou com marcadores não preenchidos.
- Qualquer item bloqueante do checklist do revisor falha na entrega.
