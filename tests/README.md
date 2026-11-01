# Sessões de teste

Carteiras-exemplo com **comportamento esperado**. Como os dados de mercado mudam todo dia, os testes verificam o **método** (fluxo, portas, fontes, linguagem, completude), não valores numéricos.

## Como rodar

1. Abra o repositório na LLM a testar (Claude Code, Cursor, Codex, ChatGPT com repositório conectado).
2. Cole a mensagem da seção **Entrada** do teste. Responda ao grill-me com as **Respostas do usuário**.
3. Ao final, confira cada item de **Comportamento esperado** e **Reprova se**.
4. Registre o resultado na tabela abaixo (no PR ou em `tests/resultados.md`, sem dados pessoais).

## Critério de aprovação de uma LLM

A LLM "executa o fluxo completo" (métrica do PRD) se passar nos testes 01, 02, 05 e 07 sem nenhum item de **Reprova se**.

## Registro

| Data | LLM / ferramenta | Teste | Resultado | Observações |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |
