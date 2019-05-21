#!/bin/bash
if command -v python3 &>/dev/null; then
    if [ -f main.py -a -f gerenciaArquivo.py -a -f validacaoTags.py ]; then
        python3 main.py
	find . -type f -name "*.py[co]" -delete
        find . -type d -name "__pycache__" -delete
    else
        echo [ERROR] Algum arquivo esta faltando! Arquivos necessarios: main.py gerenciaArquivo.py validacaoTags.py
    fi
else
    echo [ERROR] Python 3 nao instalado no computador!
fi
