#!/usr/bin/env python3
"""Gera PDF a partir do relatório HTML usando um navegador Chromium em modo headless.

Uso:
    python scripts/gerar_pdf.py session/relatorio-2026-11-02-0932-TAEE4-VIVT3.html [saida.pdf]

Sem o segundo argumento, o PDF leva o mesmo nome-base do HTML (data, hora e ativos).

Sem dependências Python: usa Chrome, Edge, Chromium ou o chrome-headless-shell do Playwright
já instalados. Tenta cada navegador encontrado, em ordem, até um gerar o PDF.
Para dar preferência a um navegador, defina a variável de ambiente CHROME_PATH: ele é tentado
primeiro, e os demais servem de alternativa se ele falhar.
"""

import glob
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NOMES_NO_PATH = [
    "google-chrome", "google-chrome-stable", "chrome", "chromium", "chromium-browser",
    "msedge", "microsoft-edge", "microsoft-edge-stable", "chrome-headless-shell",
]

CAMINHOS_CONHECIDOS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]

# chrome-headless-shell instalado pelo Playwright: em alguns ambientes (contêineres Linux)
# o Chromium completo trava no --print-to-pdf e o headless-shell funciona.
PADROES_HEADLESS_SHELL = [
    "/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell",
    os.path.expanduser("~/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell"),
    os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell"),
    os.path.expandvars(r"%LOCALAPPDATA%\ms-playwright\chromium_headless_shell-*\*\chrome-headless-shell.exe"),
]

TEMPO_LIMITE = 60  # segundos por navegador


def encontrar_navegadores():
    encontrados = []
    preferido = os.environ.get("CHROME_PATH")
    if preferido and Path(preferido).exists():
        encontrados.append(preferido)
    for nome in NOMES_NO_PATH:
        caminho = shutil.which(nome)
        if caminho:
            encontrados.append(caminho)
    encontrados += [c for c in CAMINHOS_CONHECIDOS if Path(c).exists()]
    for padrao in PADROES_HEADLESS_SHELL:
        encontrados += sorted(glob.glob(padrao), reverse=True)
    vistos, unicos = set(), []
    for caminho in encontrados:
        real = os.path.realpath(caminho)
        if real not in vistos:
            vistos.add(real)
            unicos.append(caminho)
    return unicos


def gerar(navegador, html, pdf):
    with tempfile.TemporaryDirectory() as perfil:
        comando = [navegador]
        if "headless-shell" not in Path(navegador).name:
            comando.append("--headless=new")
        # Como root (contêineres Linux), o Chromium exige --no-sandbox.
        if hasattr(os, "geteuid") and os.geteuid() == 0:
            comando.append("--no-sandbox")
        comando += [
            "--disable-gpu",
            "--no-first-run",
            f"--user-data-dir={perfil}",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf}",
            html.as_uri(),
        ]
        try:
            subprocess.run(comando, check=True, capture_output=True, timeout=TEMPO_LIMITE)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as erro:
            print(f"Falhou com {navegador}: {erro.__class__.__name__}")
            return False
    return pdf.is_file() and pdf.stat().st_size > 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2

    html = Path(argv[1]).resolve()
    if not html.is_file():
        print(f"Erro: arquivo não encontrado: {html}")
        return 1

    if "{{" in html.read_text(encoding="utf-8"):
        print("Erro: o HTML ainda tem marcadores {{...}} não preenchidos. Preencha o template antes de gerar o PDF.")
        return 1

    pdf = Path(argv[2]).resolve() if len(argv) > 2 else html.with_suffix(".pdf")

    navegadores = encontrar_navegadores()
    if not navegadores:
        print(
            "Nenhum navegador Chromium encontrado (Chrome, Edge, Chromium ou chrome-headless-shell).\n"
            "Alternativas: defina CHROME_PATH, use a ferramenta de PDF da sua LLM, ou abra o HTML "
            "no navegador → Imprimir → Salvar como PDF."
        )
        return 1

    for navegador in navegadores:
        if pdf.exists():
            pdf.unlink()
        if gerar(navegador, html, pdf):
            print(f"PDF gerado: {pdf} (com {navegador})")
            return 0

    print(
        "Erro: nenhum navegador conseguiu gerar o PDF.\n"
        "Alternativas: defina CHROME_PATH, use a ferramenta de PDF da sua LLM, ou abra o HTML "
        "no navegador → Imprimir → Salvar como PDF."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
