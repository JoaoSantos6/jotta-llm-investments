# Rule — Privacidade

> Revisado em: 2026-10-31

- A carteira do usuário só é gravada em `session/`, que está no `.gitignore`. **Nunca** escreva dados da carteira em outro lugar do repositório.
- Nunca faça commit, push ou upload de qualquer arquivo de `session/`.
- Não envie a carteira (tickers + quantidades) em consultas de busca. Busque cada ativo isoladamente, sem quantidades ou valores do usuário.
- Não peça dados pessoais (nome, CPF, corretora, patrimônio total). Quantidades e percentuais são opcionais.
- Ao iniciar uma sessão com `session/` já preenchido, pergunte se o usuário quer arquivar a sessão anterior em `session/_arquivo/AAAA-MM-DD/` (local) ou apagá-la.
