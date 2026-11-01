#!/usr/bin/env python3
"""Gera PDF a partir do relatório HTML usando um navegador Chromium em modo headless.

Uso:
    python scripts/gerar_pdf.py session/relatorio.html [saida.pdf]

Sem dependências Python: usa Chrome, Edge ou Chromium já instalado.
Para forçar um navegador, defina a variável de ambiente CHROME_PATH.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

NOMES_NO_PATH = [
    "google-chrome", "google-chrome-stable", "chrome", "chromium", "chromium-browser",
    "msedge", "microsoft-edge", "microsoft-edge-stable",
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


def encontrar_navegador():
    forcado = os.environ.get("CHROME_PATH")
    if forcado:
        return forcado if Path(forcado).exists() else None
    for nome in NOMES_NO_PATH:
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    for caminho in CAMINHOS_CONHECIDOS:
        if Path(caminho).exists():
            return caminho
    return None


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

    navegador = encontrar_navegador()
    if not navegador:
        print(
            "Nenhum navegador Chromium encontrado (Chrome, Edge ou Chromium).\n"
            "Alternativas: defina CHROME_PATH, use a ferramenta de PDF da sua LLM, ou abra o HTML "
            "no navegador → Imprimir → Salvar como PDF."
        )
        return 1

    with tempfile.TemporaryDirectory() as perfil:
        comando = [
            navegador,
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            f"--user-data-dir={perfil}",
            "--no-pdf-header-footer",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf}",
            html.as_uri(),
        ]
        try:
            subprocess.run(comando, check=True, capture_output=True, timeout=120)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as erro:
            print(f"Erro ao gerar PDF com {navegador}: {erro}")
            return 1

    if not pdf.is_file() or pdf.stat().st_size == 0:
        print("Erro: o navegador terminou sem gerar o PDF.")
        return 1

    print(f"PDF gerado: {pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
