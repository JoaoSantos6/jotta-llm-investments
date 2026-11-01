# Rule — Escrita para o leitor

> Revisado em: 2026-11-01

Quem lê o relatório quer saber duas coisas: **meus ativos estão bem?** e **existe alguma ameaça à frente?** Essa pessoa não sabe, e não precisa saber, como o framework funciona por dentro. Esta rule vale para tudo que o usuário lê: `session/relatorio.md`, a versão de chat, o HTML e o PDF.

Os arquivos de trabalho (`session/dados/`, `session/analise/`, `session/revisao.md`, `session/log.md`) continuam técnicos e completos. São eles que o revisor audita.

## 1. O framework é invisível

Nunca apareça no texto para o usuário:

| Não escreva | Escreva no lugar |
| --- | --- |
| Códigos internos: `AC-02`, `FI-01`, `FT-03`, `TD-02`, `CA-06`, `Q3`, `B6`, "porta A" | O significado: "a dívida equivale a 4,2 anos de geração de caixa da operação" |
| "critério disparado", "não disparado", "limiar do framework", "pela régua do framework" | "Acima de 4 vezes, consideramos a dívida alta para uma transmissora" |
| Nomes de arquivos e pastas: `setores.md`, `knowledge/`, `criterios.md` | A informação em si, com a fonte `[n]` quando for fato de mercado |
| "Confiança: baixa", "classificação provisória" | "Leitura provisória: faltaram dados de X e Y, e o quadro pode mudar quando eles saírem" |
| Lista de tudo o que **não** acendeu alerta | Uma frase com o que está bem ("dívida, lucro e caixa estão em ordem") |
| Bloco de glossário no topo | A explicação do termo na própria frase, na primeira vez que ele aparece |

## 2. Conclusão primeiro, detalhes depois

Escreva em pirâmide invertida:

1. **Resposta direta** — no topo do relatório e no topo de cada ativo: está bem ou não, e qual a principal ameaça, em linguagem comum.
2. **Os porquês** — os fatos que sustentam essa resposta, cada um explicado.
3. **O detalhe técnico** — tabelas e indicadores para quem quiser conferir.

Quem ler só o primeiro nível precisa sair com a resposta certa.

## 2a. Brevidade inteligente: leitura rápida e "Saiba mais"

O relatório tem duas camadas, inspiradas no método de *Smart Brevity* (ver `knowledge/referencias.md`). A ideia não é cortar conteúdo. É **ordenar** o conteúdo: o essencial chega primeiro, curto e sem susto, e a parte densa fica disponível para quem quiser aprofundar.

| Camada | Para quem | O que traz |
| --- | --- | --- |
| **Leitura rápida** | Todo leitor, em 2–3 minutos | A resposta: como está a carteira, como está cada ativo, o que observar. |
| **Saiba mais** | Quem quer conferir ou entender a fundo | Tabelas, indicadores comparados, resultados, riscos completos, cenário, lacunas, fontes. |

### Blocos da leitura rápida

Cada ativo, e também a carteira, abre com os mesmos rótulos fixos, nesta ordem:

| Rótulo | O que é | Limite |
| --- | --- | --- |
| **Em uma linha.** | A coisa mais importante, numa frase com verbo forte. Responde "está bem? qual a ameaça?". | 1 frase, até 30 palavras |
| **Por que importa.** | A consequência possível para o investidor (proventos, preço, risco). | 1–2 frases |
| **Em números.** | Até 3 números que sustentam a leitura. Cada um no formato `valor [n] — o que significa e se é bom ou ruim`. | 3 itens, até 20 palavras cada |
| **O que observar.** | O próximo evento ou indicador que pode mudar o quadro, com data. | 1–2 itens |

Depois desses rótulos vem o link para o "Saiba mais" do mesmo bloco.

### Regras da camada 1

- **Limite de tamanho:**
  - cartão de cada ativo: até **80 palavras**, sem contar as referências `[n]`;
  - "Em resumo" da carteira: até **60 palavras**, mais a tabela-síntese;
  - cada item de "O que merece sua atenção": até **40 palavras**.
- **Sem tabelas**, exceto a tabela-síntese (ativo · situação · em uma frase). Sem listas de indicadores e sem contas.
- **Todo número continua explicado** (seção 3). Na camada 1, a explicação cabe na mesma linha do número.
- **Não pode contradizer a camada 2.** Todo fato da leitura rápida tem `[n]` e reaparece no "Saiba mais" com o detalhe que o sustenta.
- **Leitura provisória** e as lacunas que mudam a conclusão aparecem já na camada 1, numa frase. A lista completa fica no "Saiba mais".

### Regras da camada 2

- Contém **todo** o conteúdo obrigatório do relatório: desempenho nas três janelas, saúde financeira, qualidade, preço, o que vem pela frente, cenário, o que pode mudar o quadro, riscos, o que acompanhar, lacunas e fontes. Nada sai do relatório por causa da brevidade.
- As demais seções desta rule (número explicado, comparar e concluir, texto limpo) continuam valendo.
- Cada bloco abre com o título "Saiba mais" seguido do nome do ativo ou tema, para que o leitor saiba que entrou na parte detalhada.

### Como cada formato mostra as camadas

| Formato | Leitura rápida | Saiba mais |
| --- | --- | --- |
| Chat | Sempre presente, no topo da resposta. | Só no detalhe "completo", depois de toda a leitura rápida, sob o título "Saiba mais". |
| HTML | Primeira parte da página, com um cartão por ativo. | Cada cartão tem um **botão "Saiba mais"** que abre o detalhe do ativo. Há também um botão para abrir ou fechar todos os detalhes. |
| PDF | Primeiras páginas: o leitor tem a resposta inteira antes de virar para o detalhe. | Parte seguinte, com todo o detalhe aberto; cada ativo começa em página nova. |

## 3. Nenhum número sozinho

Todo número que aparece para o usuário vem com três partes:

1. **O fato** — o número, com fonte.
2. **O que ele mede** — em palavras simples.
3. **Por que importa** — a comparação (régua, histórico, pares) e a consequência possível para o investidor.

Exemplos:

- ❌ "Dívida líquida/EBITDA de 4,2x [12]."
- ✅ "A dívida líquida da Taesa equivale a 4,2 anos da geração de caixa da operação (EBITDA) [12]. Para uma transmissora, acima de 4 vezes já é alto: quanto maior esse número, maior a parte do caixa que vai para juros em vez de dividendos, e mais a empresa sente quando os juros sobem."

- ❌ "P/VP 1,22 [3]."
- ✅ "A cota é negociada 22% acima do valor dos imóveis do fundo (P/VP de 1,22) [3]. Quanto mais acima desse valor, mais o preço depende de o rendimento continuar alto; um corte no rendimento tende a pesar mais na cota."

- ❌ "Vacância física 14% [4]."
- ✅ "14% da área do fundo está vazia [4]. Área vazia não gera aluguel e ainda gera custo (condomínio, IPTU), então pressiona o rendimento distribuído."

### Comparar e concluir

Explicar o que o número mede não basta: o leitor precisa saber se ele é **bom ou ruim** e o que isso diz sobre a **saúde do ativo**. Para isso, todo indicador é comparado com uma referência (histórico do ativo, mediana do setor ou índice) e termina numa conclusão. O método está em `knowledge/leitura-de-indicadores.md`.

- Desempenho sempre em três janelas, **1 semana, 12 meses e 5 anos**, cada uma contra o índice de referência, seguidas de uma frase que diz o que a trajetória mostra.
- Indicadores financeiros sempre ao lado da **mediana do setor** (com os pares nomeados) e com uma leitura `favorável`, `em linha` ou `desfavorável`.
- Cada bloco fecha com uma frase de conclusão. Lista de números sem conclusão é proibida.

❌ Lista solta:

> - Cotação: R$ 12,45, queda de 3,1% no dia; +19,7% em 12 meses [1].
> - P/L de 7,69 e P/VP de 1,49 [1].
> - Dividend yield de 9,1% [1].
> - Dívida líquida consolidada de R$ 4,1 bi [1].

✅ Comparado e concluído:

> | Período | Ação | Ibovespa | Leitura |
> | --- | --- | --- | --- |
> | 1 semana | −2,0% [1] | −0,5% [2] | Oscilação de curto prazo, sem evento novo |
> | 12 meses | +19,7% [1] | +13,0% [2] | Favorável: à frente do índice |
> | 5 anos | +38% [1] | +45% [2] | Desfavorável: atrás do índice no longo prazo |
>
> **O que a trajetória mostra:** a recuperação do último ano ainda não compensou os anos anteriores; a ação acompanha de perto o banco do qual depende.
>
> | Indicador | Empresa | Setor (mediana de A, B, C) | Leitura |
> | --- | --- | --- | --- |
> | Dividend yield | 9,1% [1] | 6,5% [3] | Favorável, e o payout cabe no lucro |
> | Dívida líquida/EBITDA | 0,4x [1] | 1,8x [3] | Favorável: dívida baixa para o porte |
>
> **Saúde financeira: sólida.** Rentabilidade e proventos acima dos concorrentes, com pouca dívida. O ponto fraco é a dependência de uma única investida.

(Os números do exemplo são ilustrativos.)

### Sem especulação nem bastidores

- Nada de "provavelmente", "parece que", "deve ser" para explicar um fato. Ou a fonte diz, ou o fato vai para "O que esta análise não cobriu".
- Não narre o processo de coleta no corpo do texto ("não consegui ler o release", "a data da série é posterior à coleta"). Se uma divergência ou um dado faltante muda a conclusão, ele é resolvido no aprofundamento; se não for resolvido, vai para "O que esta análise não cobriu", com o efeito na leitura.

Use poucos números: só os que sustentam a história. Contas intermediárias, reconstruções de períodos e números redundantes ficam em `session/analise/`. Quando duas fontes divergirem, use a fonte primária ou preferencial (`knowledge/fontes.md`) no texto e registre a divergência em "O que esta análise não cobriu".

## 4. Texto limpo

- Frases curtas, uma ideia por frase. Parágrafos de até 4 linhas.
- Siglas e termos técnicos explicados na primeira vez (use `knowledge/glossario.md` como base, mas com suas palavras).
- Prefira "a empresa", "o fundo", "o título" a nomes de indicadores como sujeito da frase.
- Datas, valores e porcentagens no padrão brasileiro.
- Emojis só no rótulo de situação (🟢 🟡 🟠 🔴).

## 5. Sem "próximos passos"

O relatório termina na lista de fontes e no aviso legal. Não escreva:

- "Próximos passos", "sugestões", "posso aprofundar…", "quer que eu…?", "se quiser, analiso…";
- perguntas ao usuário no fim da entrega.

Se, durante a análise, um levantamento a mais responderia uma dúvida importante (por exemplo, a causa de uma queda, ou um dado que mudaria a situação de um ativo), **faça esse levantamento antes de entregar** (`skills/orquestrar-sessao`, passo de aprofundamento). Se não for possível obter o dado, diga isso em "O que esta análise não cobriu", sem oferecer nada.

"O que acompanhar" não é próximo passo: descreve indicadores e datas do próprio ativo e por que cada um importa.

## 6. Compliance continua valendo

Explicar por que um número importa é **descrever consequências possíveis**, não recomendar. "Mais caixa vai para juros em vez de dividendos" é permitido; "vale reduzir a posição" continua proibido (`rules/compliance-cvm.md`).
