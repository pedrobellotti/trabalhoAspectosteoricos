#!/bin/bash
if command -v python3 &>/dev/null; then
    python3 main.py
else
    echo [ERROR] Python 3 nao instalado no computador!
fi