# Sinais de alerta — quadro geral

> Revisado em: 2026-10-31 · Detalhes e limiares numéricos: `knowledge/<classe>/criterios.md`

Ponto de partida da classificação. O estado de um ativo é o **mais grave** entre os critérios disparados (ver `skills/classificar-ativo`).

| Estado | Ações | FIIs | Tesouro Direto |
| --- | --- | --- | --- |
| 🟢 Saudável | Lucro e caixa crescentes, dívida controlada, ROE consistente, governança sem ruído | Vacância baixa, contratos longos, inquilinos diversificados, rendimento estável | Taxa real acima da média histórica, prazo compatível com o objetivo |
| 🟡 Atenção | Margens comprimindo, setor cíclico em virada, alavancagem subindo, juros pouco cobertos pela operação, lucro que não vira caixa, proventos acima do lucro, diluição relevante | Vencimento de contratos relevantes, P/VP muito acima de 1, emissões frequentes | Marcação negativa relevante se houver necessidade de resgate antes do vencimento |
| 🟠 Em queda | Queda > 20% em 12m; separar ruído de mercado de deterioração de fundamentos | Rendimento cortado, cota em queda com P/VP < 1 por motivo identificável | Taxa subindo e cota caindo por mudança de expectativa de juros |
| 🔴 Perigoso | Dívida líquida/EBITDA alta com caixa queimando, operação que não cobre os juros, recuperação judicial, ressalva de auditoria, fraude | Inquilino único inadimplente, CRIs high yield com default, alavancagem alta | Prazo incompatível com a liquidez que o usuário precisa |

## Sinais transversais (qualquer classe)

| Sinal | Estado mínimo |
| --- | --- |
| Investigação de órgão regulador ou policial envolvendo a empresa/gestora | 🔴 Perigoso |
| Ressalva, abstenção ou parecer adverso de auditoria | 🔴 Perigoso |
| Atraso na entrega de demonstrações/informes obrigatórios | 🟡 Atenção |
| Troca de CEO/CFO/gestor não planejada nos últimos 6 meses | 🟡 Atenção |
| Liquidez muito baixa (volume médio diário < R$ 500 mil) | 🟡 Atenção |
| Dados insuficientes em mais da metade dos critérios | Classificação provisória (confiança baixa) |

## Como usar os limiares

Os números em `criterios.md` são **referências do framework**, não verdades de mercado. No relatório, diga qual patamar foi usado e por que ele importa, em linguagem comum e sem códigos (`rules/escrita.md`): "a cota está 22% acima do valor dos imóveis do fundo; acima de 15%, tratamos como ponto de atenção, porque o preço passa a depender mais de o rendimento continuar alto".
