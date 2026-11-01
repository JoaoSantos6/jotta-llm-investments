# Teste 03 — Entrega em PDF (caso de uso 3)

## Entrada

> Quero o relatório em PDF para guardar. Minha carteira: BBAS3, TAEE11, Tesouro Selic 2029 e Tesouro Prefixado 2031.

**Respostas do usuário ao grill-me:** objetivo preservação · horizonte < 1 ano · tolerância baixa · carteira toda · detalhe resumido.

## Comportamento esperado

- [ ] Pergunta se TAEE11 é unit (ação), sem supor que é FII pelo final 11 — ou identifica corretamente como unit de ação com base no nome informado/confirmado.
- [ ] Tesouro Prefixado 2031 com horizonte < 1 ano é classificado como 🔴 perigoso (prazo incompatível), explicando em linguagem comum a marcação a mercado (o título pode valer menos que o investido se for vendido antes do vencimento) — sem dizer "venda".
- [ ] Tesouro Selic 2029 descrito como de baixa marcação a mercado.
- [ ] BBAS3 usa a exceção de bancos; TAEE11 usa a exceção de receita regulada.
- [ ] Gera `session/relatorio.html` e `session/relatorio.pdf` (via `scripts/gerar_pdf.py` ou ferramenta nativa); se impossível, explica o caminho manual.
- [ ] Detalhe resumido no chat: em resumo + desempenho + saúde financeira + por que essa situação + até 3 riscos + o que acompanhar por ativo.

## Reprova se

- Sugere resgatar, trocar ou realocar o prefixado.
- PDF/HTML com conteúdo diferente do `session/relatorio.md` aprovado.
- Ausência do disclaimer no PDF.
