# PRD — Framework de IA para Análise de Carteiras

Oct 31, 2026 · @João Vitor

## Visão geral e problema

O produto é um repositório no GitHub que transforma qualquer LLM com acesso a arquivos em um analista de carteiras da B3. Nome: **jotta-llm-investments**. Ele não é app nem site: é um conjunto de markdowns (skills, rules, agentes e base de conhecimento) que a LLM lê e segue.

**Problema.** O investidor pessoa física com ações, FIIs e Tesouro Direto tem dados espalhados (RI, Status Invest, Funds Explorer, CVM, Tesouro) e pouca estrutura para avaliar riscos. LLMs genéricas respondem sem método, sem fontes e sem consistência entre sessões.

**Proposta.** Um framework que entrevista o usuário, busca dados atuais na internet, aplica critérios documentados por classe de ativo e entrega um relatório no chat, em HTML ou em PDF.

**Escopo do MVP:** apenas a funcionalidade de análise de carteira.

## Objetivos, não-objetivos e métricas

**Objetivos**

- Entregar, por ativo da carteira: estado atual, expectativa para os próximos 3–12 meses, cenário de mercado, impactos possíveis e riscos.
- Entregar uma visão consolidada da carteira: concentração, exposição setorial, sensibilidade a juros e inflação, alertas.
- Funcionar em qualquer LLM com acesso ao repositório e à web (Claude Code, Cursor, Codex, ChatGPT com repositório conectado).
- Toda afirmação factual vem com fonte e data de coleta.

**Não-objetivos**

- Não é app, site, API nem bot com interface própria.
- Não executa ordens, não conecta a corretoras, não move dinheiro.
- Não emite recomendação personalizada de compra/venda nem preço-alvo próprio.
- Não faz monitoramento contínuo nem alertas agendados (fora do MVP).

**Métricas de sucesso**

| Métrica | Meta MVP |
| --- | --- |
| Sessões que chegam ao relatório final | ≥ 80% |
| Afirmações factuais com fonte e data | 100% |
| Ativos da carteira com todas as seções preenchidas | ≥ 95% |
| Tempo de entrevista (grill-me) | ≤ 5 min |
| LLMs testadas que executam o fluxo completo | ≥ 3 |

## Personas e casos de uso

| Persona | Perfil | O que quer do framework |
| --- | --- | --- |
| Investidor iniciante | Até 10 ativos, aprendeu sozinho | Entender se a carteira tem algo perigoso e por quê |
| Investidor intermediário | 10–30 ativos, mistura ações, FIIs e Tesouro | Revisão periódica com riscos, eventos e cenário macro |
| Desenvolvedor / mantenedor | Contribui no repositório | Adicionar skills, critérios e fontes sem quebrar o fluxo |

**Casos de uso do MVP**

1. "Tenho PETR4, ITUB4, HGLG11, MXRF11 e Tesouro IPCA+ 2035. Analise minha carteira."
2. "Analise só meus FIIs com foco em risco de vacância e dividendos."
3. "Quero o relatório em PDF para guardar."
4. "Algum dos meus ativos está em queda forte? Isso é ruído ou problema estrutural?"

## Fluxo da sessão

Uma sessão tem quatro fases — entrevista, coleta, análise, entrega — com duas portas: o usuário confirma o briefing e o revisor aprova o relatório.

&#91;embedded content: fluxo de uma sessão · 6 etapas, 2 checagens\]

Se o briefing estiver incompleto, o grill-me volta a perguntar; se o revisor achar afirmação sem fonte ou tom de recomendação, o analista corrige antes da entrega.

## Arquitetura do repositório

Tudo é markdown: **rules** dizem o que nunca pode acontecer, **skills** dizem como fazer cada etapa, **agentes** dizem quem faz, e a **base de conhecimento** diz como julgar.

&#91;embedded content: estrutura do repositório · 6 pastas + ponto de entrada\]

Quando a LLM suporta subagentes (ex.: Claude Code), cada pesquisador roda em paralelo; quando não suporta, o orquestrador executa os papéis em sequência.

**Base de conhecimento — o que cada estado significa**

Cada classe tem seus critérios em `knowledge/<classe>/`; o quadro abaixo é o ponto de partida que `sinais-de-alerta.md` detalha.

| Estado | Ações | FIIs | Tesouro Direto |
| --- | --- | --- | --- |
| Saudável | Lucro e caixa crescentes, dívida controlada, ROE consistente, governança sem ruído | Vacância baixa, contratos longos, inquilinos diversificados, rendimento estável | Taxa real acima da média histórica, prazo compatível com o objetivo |
| Atenção | Margens comprimindo, setor cíclico em virada, alavancagem subindo | Vencimento de contratos relevantes, P/VP muito acima de 1, emissões frequentes | Marcação negativa relevante se houver necessidade de resgate antes do vencimento |
| Em queda | Queda > 20% em 12m; separar ruído de mercado de deterioração de fundamentos | Rendimento cortado, cota em queda com P/VP < 1 por motivo identificável | Taxa subindo e cota caindo por mudança de expectativa de juros |
| Perigoso | Dívida líquida/EBITDA alta com caixa queimando, recuperação judicial, ressalva de auditoria, fraude | Inquilino único inadimplente, CRIs high yield com default, alavancagem alta | Prazo incompatível com a liquidez que o usuário precisa |

## Requisitos funcionais

**RF-01 Entrada.** Um arquivo de entrada (`AGENTS.md` + `CLAUDE.md` apontando para ele) instrui qualquer LLM a carregar as rules e iniciar o grill-me ao receber "analisar carteira" ou similar.

**RF-02 Skill grill-me.** Entrevista obrigatória antes de qualquer busca. Pergunta uma coisa por vez, com opções sugeridas, e só encerra quando o briefing está completo:

- Ativos e classe (ação, FII, Tesouro); quantidade ou % da carteira (opcional)
- Objetivo: renda, crescimento, preservação
- Horizonte: < 1 ano, 1–5 anos, > 5 anos
- Tolerância a risco e preocupações específicas ("tenho medo de X")
- Foco da sessão: carteira toda, um ativo, uma classe
- Formato de saída: chat, HTML ou PDF; nível de detalhe

Saída: `session/briefing.md`, confirmado pelo usuário antes de seguir.

**RF-03 Coleta de dados.** Agentes de pesquisa por classe de ativo buscam dados na web seguindo `knowledge/fontes.md`. Cada dado sai com valor, fonte (URL), data de referência e data de coleta.

| Classe | Dados mínimos |
| --- | --- |
| Ações | Cotação e variação 12m, P/L, P/VP, ROE, dívida líq./EBITDA, margens, dividend yield, últimos resultados trimestrais, fatos relevantes, consenso de analistas (quando público) |
| FIIs | Cotação, P/VP, DY 12m, histórico de rendimentos, vacância física e financeira, inquilinos e contratos, alavancagem, gestora, emissões recentes |
| Tesouro Direto | Taxa atual e histórica, marcação a mercado, vencimento, indexador, Selic e IPCA esperados (Focus) |
| Macro | Selic, IPCA, câmbio, curva de juros, projeções do Boletim Focus |

**RF-04 Classificação do ativo.** O agente analista aplica os critérios da base de conhecimento e enquadra cada ativo em um estado: *saudável*, *atenção*, *em queda*, *perigoso* — sempre com a justificativa e os critérios disparados.

**RF-05 Análise por ativo.** Seções fixas: estado atual · expectativa 3–12 meses · cenário do setor/mercado · impactos possíveis (macro, regulatórios, específicos) · riscos · o que monitorar.

**RF-06 Análise consolidada.** Concentração por ativo, setor e classe; exposição a juros, inflação e câmbio; correlações óbvias; alertas priorizados.

**RF-07 Revisão.** Um agente revisor confere se toda afirmação tem fonte, se não há recomendação de compra/venda e se o disclaimer está presente. Reprova e devolve ao analista se algo falhar.

**RF-08 Saída.** Três renderizadores sobre o mesmo conteúdo:

- **Chat:** markdown com leitura rápida no topo e, no detalhe completo, o "Saiba mais".
- **HTML:** arquivo único autocontido a partir de `templates/relatorio.html`, com botões "Saiba mais".
- **PDF:** gerado do HTML (script em `scripts/`) ou nativo, quando a LLM tiver ferramenta para isso.
- **Entrega em arquivo:** quando o formato é HTML ou PDF, o chat recebe somente o arquivo e o aviso legal, sem repetir o conteúdo. Os arquivos levam data, hora e ativos no nome (`relatorio-AAAA-MM-DD-HHMM-TICKERS.html`).

**RF-09 Disclaimer.** Todo relatório termina com aviso de que é material informativo e não constitui recomendação de investimento.

## Requisitos não funcionais, compliance e riscos

**Não funcionais**

- **Agnóstico de LLM:** só markdown e convenções simples; nada depende de um fornecedor. Adaptadores finos (`CLAUDE.md`, `.cursor/rules`, `AGENTS.md`) apontam para o mesmo núcleo.
- **Sem dependência de API paga no MVP:** coleta via busca e leitura de páginas públicas. Integrações opcionais (brapi, APIs do Tesouro/BCB) ficam documentadas como extensão.
- **Rastreabilidade:** cada sessão gera `session/` com briefing, dados brutos coletados e relatório — tudo auditável.
- **Privacidade:** a carteira do usuário não é versionada; `session/` está no `.gitignore`.
- **Idioma:** português do Brasil em todos os arquivos e saídas.
- **Extensível:** adicionar uma skill = criar uma pasta com `SKILL.md`, sem mexer no orquestrador.

**Compliance (CVM)**

O framework não pode se apresentar como consultoria ou análise de valores mobiliários registrada (Resoluções CVM 19 e 20). Por isso, as rules proíbem "compre", "venda", preço-alvo próprio e alocação recomendada; o texto descreve fatos, cenários e riscos. Consensos de terceiros podem ser citados, com fonte.

**Riscos**

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| LLM alucina números | Alto | Rule: nenhum número sem fonte; revisor reprova |
| Dados defasados ou fontes bloqueadas | Médio | Data de coleta visível; lista de fontes alternativas por dado |
| Tom de recomendação | Alto (regulatório) | Rule de linguagem + checklist do revisor + disclaimer |
| Comportamento diferente entre LLMs | Médio | Instruções explícitas e passo a passo; suíte de sessões de teste |
| Base de conhecimento desatualizada | Médio | Versionamento, data de revisão em cada arquivo, CONTRIBUTING |
| Contexto longo em carteiras grandes | Médio | Subagentes por ativo quando suportado; senão, lotes de 5 ativos |

## Roadmap e questões em aberto

1. **v0.1 — Núcleo:** `AGENTS.md`, rules, grill-me, orquestrador e saída em chat. Base de conhecimento de ações.
2. **v0.2 — Cobertura completa:** base de FIIs, Tesouro e macro; agentes de pesquisa por classe; revisor.
3. **v0.3 — Relatórios:** template HTML e geração de PDF; adaptadores para Claude Code, Cursor e Codex.
4. **v1.0 — Estável:** sessões de teste (carteiras-exemplo com resultado esperado), CONTRIBUTING, versionamento da base.
5. **Pós-MVP (ideias):** comparação entre sessões, rebalanceamento hipotético, BDRs/ETFs, cripto.

**Questões em aberto**

- [ ] Nome definitivo do repositório e licença (MIT, Apache 2.0 ou CC BY-NC para a base de conhecimento?).
- [ ] Aceitar arquivo de extrato (CSV/PDF da corretora ou da B3) como entrada, além do texto no chat?
- [ ] Incluir valuation simples (ex.: Bazin, Graham) como referência descritiva ou deixar fora para evitar tom de recomendação?
- [ ] Quais fontes são oficiais do MVP e qual o fallback quando uma bloqueia leitura automática?
- [ ] O relatório deve guardar histórico para comparar com sessões futuras?
