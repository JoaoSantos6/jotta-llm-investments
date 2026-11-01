# Rule — Compliance CVM (linguagem)

> Revisado em: 2026-10-31

O framework **não é** consultoria nem análise de valores mobiliários registrada (Resoluções CVM 19 e 20). O texto descreve fatos, cenários e riscos — nunca orienta decisões.

## Proibido

| Proibido | Exemplos | Alternativa permitida |
| --- | --- | --- |
| Ordem ou sugestão de operação | "compre", "venda", "mantenha", "aumente posição", "realize lucro", "hora de entrar", "aproveite a queda" | "O ativo está em *atenção*: a dívida equivale a 4,2 anos de geração de caixa, acima do patamar considerado alto para o setor." |
| Preço-alvo ou valor justo próprio | "o preço justo é R$ 40", "upside de 30%" | Citar consenso de terceiros com fonte: "Consenso de N analistas compilado por <fonte> em <data>: R$ X." |
| Alocação recomendada | "deixe 20% em FIIs", "reduza ações para 30%" | "FIIs representam 45% da carteira. Acima de 40% numa única classe, um mesmo fator (como a Selic) passa a mover boa parte do patrimônio." |
| Juízo de oportunidade | "está barato", "está caro", "oportunidade", "pechincha", "imperdível" | "P/VP de 0,82, abaixo da média de 5 anos do próprio fundo (0,97) segundo <fonte>." |
| Previsão afirmativa | "vai subir", "vai cortar dividendo" | "Cenário possível: … ; gatilho a monitorar: …" |
| Valuation próprio (Bazin, Graham, DCF) | "pelo Graham vale R$ 25" | Fora do MVP. Apenas múltiplos de mercado com fonte. |
| Triagem ou método de seleção como veredito | "passa no filtro de Bazin", "está na Fórmula Mágica", "aprovada nos critérios de qualidade" | Descrever os indicadores individualmente, com fonte. Critérios do framework descrevem alertas, não aprovam ativos. |
| Juízo sobre múltiplos | "múltiplo esticado", "negociando com desconto", "barato para o setor" | "P/L de 8,2 [n], abaixo da média de 5 anos do ativo (11,4) [n] e da mediana de 3 pares (10,1) [n]. O mercado paga menos por cada real de lucro do que pelos concorrentes, o que costuma refletir percepção de risco: …" (conclusões de `knowledge/leitura-de-indicadores.md`) |

## Permitido

- Descrever indicadores, eventos, fatos relevantes e o estado do ativo pelos critérios documentados.
- Cenários condicionais ("se a Selic permanecer acima de X%, FIIs de papel atrelados ao CDI tendem a …"), sempre como possibilidade.
- Citar recomendações e preços-alvo **de terceiros**, identificando quem, quando e onde, sem endossar. Prefira o agregado de várias casas (ex.: "das 8 casas compiladas por <fonte> em <data>, 5 com recomendação positiva, 3 neutras") a uma recomendação isolada.
- Apontar riscos e "o que monitorar".
- Comparar indicadores com setor, histórico e índices e concluir sobre a **saúde financeira** do ativo (sólida, com pontos de atenção, frágil). É descrição do estado do negócio, não indicação de compra ou venda.

## Pedidos diretos de recomendação

Se o usuário perguntar "devo vender?", "compro mais?", "qual o preço-alvo?":

1. Explique, em uma frase, que o framework não faz recomendação personalizada (CVM 19/20).
2. Ofereça o que é permitido: o estado do ativo, os riscos, os gatilhos a monitorar e o consenso público de terceiros.
3. Sugira, se fizer sentido, procurar um profissional certificado (CNPI para análise, consultor CVM para consultoria).

## Disclaimer

Todo relatório, em qualquer formato, termina com o texto de [`templates/disclaimer.md`](../templates/disclaimer.md), sem alterações.
