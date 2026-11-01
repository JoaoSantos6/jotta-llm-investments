# Teste 08 — Brevidade inteligente (leitura rápida + "Saiba mais")

## Entrada

> Traga um balanço da minha carteira: TAEE11, ITSA4, BBSE3 e VIVT3.

**Respostas do usuário ao grill-me:** não informar pesos · objetivo crescimento · horizonte > 5 anos · tolerância média · sem preocupação específica · carteira toda · HTML · completo.

Depois da entrega, peça também a versão em PDF e, em outra rodada, a versão no chat com detalhe "resumido".

## Comportamento esperado

- [ ] O relatório canônico tem a "Leitura rápida" inteira antes do "Saiba mais".
- [ ] A carteira abre com "Em uma linha" e "Por que importa" (até 60 palavras), seguidos da tabela-síntese.
- [ ] Cada ativo tem um cartão de até 80 palavras, com "Em uma linha", "Por que importa", "Em números" (até 3 itens, cada número com o que significa) e "O que observar" (com data).
- [ ] A leitura rápida não tem tabelas além da síntese.
- [ ] Quem lê só a leitura rápida fica sabendo:
  - quais ativos estão bem e quais pedem atenção;
  - a principal ameaça de cada um;
  - quais lacunas mudam a conclusão.
- [ ] Todo fato da leitura rápida reaparece, com o detalhe, no "Saiba mais" do mesmo ativo.
- [ ] O "Saiba mais" de cada ativo tem todas as seções obrigatórias:
  - desempenho em três janelas, saúde financeira, qualidade e preço;
  - o que vem pela frente, setor e cenário, o que pode mudar o quadro;
  - riscos e o que acompanhar.
- [ ] **HTML:**
  - cada cartão tem um botão "Saiba mais" que abre o detalhe do ativo, e o detalhe tem "Voltar à leitura rápida";
  - clicar numa linha da tabela-síntese abre o detalhe do ativo;
  - há um botão para abrir e fechar todos os detalhes;
  - clicar numa referência `[n]` mostra a fonte;
  - sem JavaScript, todo o detalhe aparece aberto;
  - o arquivo não carrega nenhum recurso externo.
- [ ] **PDF:** a leitura rápida ocupa as primeiras páginas; o "Saiba mais" começa em página nova, todo aberto, sem botões.
- [ ] **Chat "resumido":** só a leitura rápida, com limites desta leitura, fontes citadas e aviso legal.
- [ ] **Chat "completo":** a leitura rápida inteira e depois o bloco "Saiba mais".

## Reprova se

- Um cartão de ativo passa de 80 palavras, ou "Em números" tem mais de 3 itens.
- A leitura rápida contradiz o "Saiba mais", ou traz um fato que o "Saiba mais" não sustenta.
- Alguma seção obrigatória do ativo some do relatório "em nome da brevidade".
- A leitura provisória de um ativo só aparece no "Saiba mais".
- O HTML esconde o detalhe sem botão para abri-lo, ou o PDF sai com detalhes fechados.
- Aparece um número na leitura rápida sem dizer o que significa.
