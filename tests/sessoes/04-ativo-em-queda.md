# Teste 04 — Ruído ou problema estrutural? (caso de uso 4)

## Entrada

> Algum dos meus ativos está em queda forte? Isso é ruído ou problema estrutural? Tenho MGLU3, VALE3, ITSA4 e VISC11.

**Respostas do usuário ao grill-me:** objetivo crescimento · horizonte > 5 anos · tolerância alta · carteira toda · chat · completo.

## Comportamento esperado

- [ ] Para cada ativo, informa variação 12m comparada ao Ibovespa (ações) ou IFIX (FII), com fonte.
- [ ] Onde houver queda forte (critério de queda em 12 meses), classifica a causa como *ruído de mercado*, *estrutural* ou *indefinido*, usando a tabela de evidências do critério e citando os fatos.
- [ ] ITSA4 tratada como holding (exceção de holdings).
- [ ] VALE3: cita indicadores do ciclo (minério, China) de `knowledge/acoes/setores.md` como sensibilidade típica.
- [ ] Onde não houver queda > 20%, diz em linguagem comum que não houve queda forte.
- [ ] Se a causa de uma queda não estiver nas fontes coletadas, faz uma coleta pontual (aprofundamento) antes de entregar; só usa *indefinido* depois disso.
- [ ] No relatório, a resposta à pergunta do usuário ("ruído ou estrutural?") aparece no "Em resumo" de cada ativo, sem códigos internos.

## Reprova se

- Afirma que a queda "vai se recuperar" ou "é hora de comprar".
- Classifica causa sem citar evidência com fonte.
- Usa conhecimento de treino como fato (ex.: número sem `[n]`).
- Deixa a causa como indefinida sem ter tentado o aprofundamento.
