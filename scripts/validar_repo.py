#!/usr/bin/env python3
"""Valida a consistência do repositório jotta-llm-investments (para mantenedores e CI).

Uso:
    python scripts/validar_repo.py

Checa: frontmatter das skills, agentes referenciados, data de revisão em rules/knowledge,
links relativos em markdown, marcadores do template HTML, ausência de códigos internos
nos templates do leitor, rótulos de brevidade inteligente, sessões de teste e .gitignore.
Sai com código 1 se houver erro.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAMPOS_SKILL = ["nome", "descricao", "papel", "entradas", "saidas"]
MARCADORES_HTML = [
    "TITULO", "META", "RESUMO", "ALERTAS", "SINTESE_LINHAS", "CARTOES", "CARTEIRA_BREVE",
    "LIMITES", "MACRO", "ATIVOS", "CONSOLIDADA", "LACUNAS", "FONTES", "DISCLAIMER",
]
# Brevidade inteligente (rules/escrita.md, seção 2a): rótulos que todo template de relatório precisa ter
ROTULOS_BREVIDADE = ["Em uma linha", "Por que importa", "Em números", "O que observar", "Saiba mais"]
TEMPLATES_RELATORIO = ["relatorio.md", "relatorio-chat.md", "relatorio.html"]
TEMPLATES_LEITOR = ["relatorio.md", "relatorio-chat.md", "relatorio.html", "disclaimer.md"]
CODIGO_INTERNO = re.compile(r"\b(?:AC|FI|FT|FP|FO|FH|TD|CA)-\d+\b|\bQ[1-7]\b")
SECOES_TESTE = ["## Entrada", "## Comportamento esperado", "## Reprova se"]
PASTAS_IGNORADAS = {".git", "session", "node_modules", "__pycache__"}

erros = []


def erro(arquivo, mensagem):
    erros.append(f"{arquivo.relative_to(RAIZ).as_posix()}: {mensagem}")


def arquivos_md():
    for caminho in RAIZ.rglob("*.md"):
        if not PASTAS_IGNORADAS.intersection(caminho.relative_to(RAIZ).parts):
            yield caminho


def ler_frontmatter(texto):
    bloco = re.match(r"^---\n(.*?)\n---\n", texto.replace("\r\n", "\n"), re.S)
    if not bloco:
        return None
    campos = {}
    for linha in bloco.group(1).splitlines():
        if ":" in linha:
            chave, valor = linha.split(":", 1)
            campos[chave.strip()] = valor.strip()
    return campos


def validar_skills():
    for pasta in sorted((RAIZ / "skills").iterdir()):
        if not pasta.is_dir():
            continue
        skill = pasta / "SKILL.md"
        if not skill.is_file():
            erro(pasta, "pasta de skill sem SKILL.md")
            continue
        campos = ler_frontmatter(skill.read_text(encoding="utf-8"))
        if campos is None:
            erro(skill, "sem frontmatter")
            continue
        for campo in CAMPOS_SKILL:
            if not campos.get(campo):
                erro(skill, f"frontmatter sem '{campo}'")
        if campos.get("nome") and campos["nome"] != pasta.name:
            erro(skill, f"nome '{campos['nome']}' difere da pasta '{pasta.name}'")
        for agente in re.findall(r"agents/[\w-]+\.md", campos.get("papel", "")):
            if not (RAIZ / agente).is_file():
                erro(skill, f"agente inexistente: {agente}")


def validar_revisao():
    for pasta in ("rules", "knowledge"):
        for caminho in (RAIZ / pasta).rglob("*.md"):
            if not re.search(r"Revisado em: \d{4}-\d{2}-\d{2}", caminho.read_text(encoding="utf-8")):
                erro(caminho, "sem linha 'Revisado em: AAAA-MM-DD'")


def validar_links():
    padrao = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for caminho in arquivos_md():
        for alvo in padrao.findall(caminho.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#)", alvo):
                continue
            destino = (caminho.parent / alvo.split("#")[0]).resolve()
            if not destino.exists():
                erro(caminho, f"link quebrado: {alvo}")


def validar_entrada():
    agents_md = (RAIZ / "AGENTS.md").read_text(encoding="utf-8")
    for regra in sorted((RAIZ / "rules").glob("*.md")):
        if f"rules/{regra.name}" not in agents_md:
            erro(RAIZ / "AGENTS.md", f"não carrega rules/{regra.name}")
    for adaptador in ("CLAUDE.md", ".cursor/rules/jotta-llm-investments.mdc"):
        caminho = RAIZ / adaptador
        if not caminho.is_file() or "AGENTS.md" not in caminho.read_text(encoding="utf-8"):
            erro(RAIZ / "AGENTS.md", f"adaptador ausente ou sem apontar para AGENTS.md: {adaptador}")


def validar_template_html():
    caminho = RAIZ / "templates" / "relatorio.html"
    texto = caminho.read_text(encoding="utf-8")
    for marcador in MARCADORES_HTML:
        if "{{" + marcador + "}}" not in texto:
            erro(caminho, f"marcador ausente: {{{{{marcador}}}}}")
    sem_comentarios = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    if re.search(r"<(script|link)\b[^>]*(src|href)=\"https?:", sem_comentarios):
        erro(caminho, "template carrega recurso externo (deve ser autocontido)")


def validar_templates_leitor():
    """Templates que o usuário lê não podem carregar códigos internos (rules/escrita.md)."""
    for nome in TEMPLATES_LEITOR:
        caminho = RAIZ / "templates" / nome
        for codigo in sorted(set(CODIGO_INTERNO.findall(caminho.read_text(encoding="utf-8")))):
            erro(caminho, f"código interno no template do leitor: {codigo}")


def validar_brevidade():
    """Templates de relatório trazem os rótulos da leitura rápida e o "Saiba mais"."""
    for nome in TEMPLATES_RELATORIO:
        caminho = RAIZ / "templates" / nome
        texto = caminho.read_text(encoding="utf-8")
        for rotulo in ROTULOS_BREVIDADE:
            if rotulo not in texto:
                erro(caminho, f"rótulo de brevidade ausente: '{rotulo}'")
    html = (RAIZ / "templates" / "relatorio.html").read_text(encoding="utf-8")
    if 'class="saiba"' not in re.sub(r"<!--.*?-->", "", html, flags=re.S):
        erro(RAIZ / "templates" / "relatorio.html", "template sem botão 'Saiba mais' (class=\"saiba\")")


def validar_testes():
    sessoes = sorted((RAIZ / "tests" / "sessoes").glob("*.md"))
    if not sessoes:
        erro(RAIZ / "tests", "nenhuma sessão de teste em tests/sessoes/")
    for caminho in sessoes:
        texto = caminho.read_text(encoding="utf-8")
        for secao in SECOES_TESTE:
            if secao not in texto:
                erro(caminho, f"seção ausente: {secao}")


def validar_gitignore():
    caminho = RAIZ / ".gitignore"
    linhas = caminho.read_text(encoding="utf-8").splitlines() if caminho.is_file() else []
    if not any(linha.strip().strip("/") == "session" for linha in linhas):
        erro(RAIZ / "AGENTS.md", ".gitignore não ignora session/")


def main():
    validar_skills()
    validar_revisao()
    validar_links()
    validar_entrada()
    validar_template_html()
    validar_templates_leitor()
    validar_brevidade()
    validar_testes()
    validar_gitignore()
    if erros:
        print(f"{len(erros)} problema(s) encontrado(s):")
        for item in erros:
            print(f"  - {item}")
        return 1
    print("Repositório válido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
