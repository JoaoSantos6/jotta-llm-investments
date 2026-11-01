# Contribuindo com o jotta-llm-investments

Obrigado! Tudo aqui é markdown, então contribuir é escrever com método.

## Princípios

- **Português do Brasil** em todos os arquivos.
- **Agnóstico de LLM:** nada que dependa de um fornecedor. Instruções específicas ficam nos adaptadores (`CLAUDE.md`, `.cursor/rules/`).
- **Compliance primeiro:** nenhuma mudança pode introduzir linguagem de recomendação (`rules/compliance-cvm.md`).
- **Leitor primeiro:** códigos de critério (AC-01, Q3…) são internos. Templates do relatório não podem tê-los, e o validador checa isso (`rules/escrita.md`).
- **Sem dados pessoais:** nunca inclua carteiras reais em exemplos, testes ou issues.

## Tipos de contribuição

### Nova skill
1. Crie `skills/<nome>/SKILL.md` com o frontmatter: `nome` (igual à pasta), `descricao`, `papel` (arquivo(s) em `agents/`), `entradas`, `saidas`.
2. Se a skill entra no fluxo padrão, adicione um passo em `skills/orquestrar-sessao/SKILL.md`. Skills independentes não precisam mexer no orquestrador.

### Novo critério ou ajuste de limiar
1. Edite `knowledge/<classe>/criterios.md` mantendo o padrão de ID (`AC-`, `FI-`, `FT-`, `FP-`, `TD-`, `CA-`).
2. Justifique o limiar no PR (referência, prática de mercado ou literatura).
3. Atualize `Revisado em:` do arquivo e registre no `CHANGELOG.md`.

### Nova fonte
1. Adicione em `knowledge/fontes.md` na posição certa da hierarquia (oficial → agregador → imprensa), com fallback.
2. Fontes pagas ou com login entram só em "Extensões opcionais".

### Nova classe de ativo (pós-MVP: BDRs, ETFs, cripto)
Crie `knowledge/<classe>/criterios.md`, um agente `agents/pesquisador-<classe>.md`, a coluna em `knowledge/sinais-de-alerta.md`, a seção em `knowledge/fontes.md` e ao menos uma sessão de teste.

## Antes de abrir o PR

- [ ] `python scripts/validar_repo.py` passa.
- [ ] Rodou ao menos a sessão de teste afetada (`tests/sessoes/`) em uma LLM e registrou o resultado no PR.
- [ ] Atualizou `Revisado em:` dos arquivos de `rules/` e `knowledge/` que mudaram.
- [ ] Atualizou o `CHANGELOG.md`.

## Versionamento da base

A base de conhecimento segue [SemVer](https://semver.org/lang/pt-BR/) junto com o repositório:
- **major:** muda o fluxo, as portas ou o formato dos artefatos de `session/`;
- **minor:** novos critérios, fontes, skills ou classes;
- **patch:** ajustes de texto, limiares pontuais, correções.
