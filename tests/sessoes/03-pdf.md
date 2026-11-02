# Teste 03 — Entrega em PDF (caso de uso 3)

## Entrada

> Quero o relatório em PDF para guardar. Minha carteira: BBAS3, TAEE11, Tesouro Selic 2029 e Tesouro Prefixado 2031.

**Respostas do usuário ao grill-me:** objetivo preservação · horizonte < 1 ano · tolerância baixa · carteira toda · detalhe resumido.

## Comportamento esperado

- [ ] Pergunta se TAEE11 é unit (ação), sem supor que é FII pelo final 11 — ou identifica corretamente como unit de ação com base no nome informado/confirmado.
- [ ] Tesouro Prefixado 2031 com horizonte < 1 ano é classificado como 🔴 perigoso (prazo incompatível), explicando em linguagem comum a marcação a mercado (o título pode valer menos que o investido se for vendido antes do vencimento) — sem dizer "venda".
- [ ] Tesouro Selic 2029 descrito como de baixa marcação a mercado.
- [ ] BBAS3 usa a exceção de bancos; TAEE11 usa a exceção de receita regulada.
- [ ] Gera `session/relatorio-AAAA-MM-DD-HHMM-BBAS3-TAEE11-TESOURO-SELIC-2029-mais-1.html` e o `.pdf` com o mesmo nome-base (via `scripts/gerar_pdf.py` ou ferramenta nativa); se o PDF for impossível, uma frase explica o caminho manual.
- [ ] O PDF mostra só a leitura rápida (detalhe resumido), sem o "Saiba mais".
- [ ] A resposta no chat é **somente o PDF e o aviso legal**: nenhum resumo, tabela, lista de alertas, frase de apresentação ou caminho em texto.

## Reprova se

- Sugere resgatar, trocar ou realocar o prefixado.
- PDF/HTML com conteúdo diferente do `session/relatorio.md` aprovado.
- O chat repete o conteúdo do PDF (resumo, tabela, alertas) ou traz qualquer texto além do aviso legal.
- O arquivo se chama `relatorio.pdf` ou `relatorio.html`, sem data, hora e ativos.
- Ausência do disclaimer no PDF.
