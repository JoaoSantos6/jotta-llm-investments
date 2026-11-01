---
nome: coletar-dados
descricao: Busca na web os dados mínimos de cada ativo e do cenário macro, com fonte e datas, gravando um arquivo por ativo.
papel: agents/pesquisador-acoes.md, agents/pesquisador-fiis.md, agents/pesquisador-tesouro.md, agents/pesquisador-macro.md
entradas: session/briefing.md (confirmado), lote de ativos
saidas: session/dados/<ATIVO>.md e session/dados/macro.md
---

# Skill — Coletar dados

## Pré-condição

`session/briefing.md` com `status: confirmado`. Caso contrário, **pare** e volte ao grill-me.

## Passo a passo (por ativo)

1. Leia o arquivo do seu agente em `agents/` e a seção da classe em [`knowledge/fontes.md`](../../knowledge/fontes.md).
2. Para cada **dado mínimo** da classe (lista no arquivo do agente), busque na fonte primária indicada; se bloquear ou não tiver o dado, use o fallback na ordem listada.
3. Registre cada dado com valor, fonte (URL exata da página lida), data de referência e data de coleta — formato em [`templates/dados-coletados.md`](../../templates/dados-coletados.md).
4. Colete também **eventos dos últimos 12 meses**: fatos relevantes, comunicados, resultados, emissões, mudanças de gestão, processos — cada um com data e link.
5. Registre lacunas: dado `não encontrado` + fontes tentadas; divergências > 5% entre fontes.
6. Grave `session/dados/<ATIVO>.md` (Tesouro: `session/dados/TESOURO-IPCA-2035.md`, sem espaços nem `+`).

## Boas práticas de busca

- Busque **um ativo por vez**, sem dados do usuário na consulta (`rules/privacidade.md`).
- Prefira abrir a página da fonte a confiar no trecho do buscador. O trecho do buscador **não** é fonte.
- Use consultas específicas: `HGLG11 relatório gerencial setembro 2026`, `PETR4 resultado 2T26 release`.
- Não copie opinião de terceiros como fato. Opinião/recomendação de casas de análise vai na seção "Consenso de terceiros", identificada.

## Limites

- Máximo de ~8 páginas lidas por ativo (~12 para ações, por causa do Formulário de Referência e da DFC). Se ainda faltar dado mínimo, registre a lacuna e siga.
- Do Formulário de Referência, leia só as seções necessárias (histórico, atividades, controle, administração, partes relacionadas, fatores de risco) e resuma com suas palavras.
- Não calcule indicadores que a fonte não informa, exceto variações simples (ex.: variação de 12m a partir de duas cotações citadas), mostrando a conta e as duas fontes.
