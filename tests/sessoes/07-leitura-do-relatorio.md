# Teste 07 — Relatório legível para o investidor

## Entrada

> Analisa minha carteira: TAEE11, ITSA4 e BBAS3. Quero saber se estão bem.

**Respostas do usuário ao grill-me:** objetivo renda · horizonte 1–5 anos · tolerância média · sem preocupação específica · carteira toda · chat · completo.

## Comportamento esperado

- [ ] O relatório abre com um "Em resumo" de 2–4 frases que diz quais ativos estão bem, quais pedem atenção e qual a principal ameaça, seguido da tabela ativo · situação · em uma frase.
- [ ] Cada ativo abre com um "Em resumo" que responde: está bem hoje? há ameaça à frente?
- [ ] Todo número que justifica uma situação, alerta ou risco vem com o que ele mede e por que importa (ex.: dívida líquida/EBITDA explicada como "anos de geração de caixa para pagar a dívida" e o efeito sobre juros e dividendos).
- [ ] Cada ativo mostra desempenho em 1 semana, 12 meses e 5 anos contra o Ibovespa (e o índice do setor quando existir: IEE para TAEE11, IFNC para ITSA4 e BBAS3), com a leitura de cada janela e uma frase sobre a trajetória.
- [ ] Cada ativo tem a tabela de saúde financeira contra a mediana de pares nomeados (BBAS3 com Basileia e inadimplência no lugar de dívida/EBITDA) e a conclusão sólida / com pontos de atenção / frágil.
- [ ] Múltiplos vêm com a conclusão sobre o que o preço embute, sem "barato" ou "caro".
- [ ] Cada dado do cenário econômico diz qual dos três ativos ele afeta e em que direção.
- [ ] Os sinais que não acenderam alerta aparecem, no máximo, em uma frase sobre o que está em ordem.
- [ ] Contas intermediárias e divergências entre fontes ficam fora do corpo do texto (divergências em "O que esta análise não cobriu").
- [ ] Se alguma dúvida importante surgiu na análise (ex.: queda sem causa nas fontes), o log mostra uma coleta pontual antes da revisão, e o resultado aparece no relatório.
- [ ] A resposta termina no aviso legal.

## Reprova se

- Aparece qualquer código interno (AC-, FI-, TD-, CA-, Q1–Q7), "critério disparado", "limiar do framework", "classificação provisória" ou nome de arquivo do repositório no texto para o usuário.
- Um indicador aparece sem explicação do que mede ou de por que é bom ou ruim.
- Aparece uma lista de números sem comparação nem conclusão (ex.: "P/L de 7,7 e P/VP de 1,5" sozinhos).
- Usa "provavelmente" ou narra a coleta no corpo do texto ("não consegui ler o release").
- O relatório traz um bloco de glossário no topo em vez de explicar os termos no texto.
- A resposta termina com "próximos passos", oferta de aprofundamento ("posso…", "quer que eu…") ou pergunta ao usuário.
