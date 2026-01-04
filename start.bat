@echo off
REM Ativa o ambiente virtual, se houver
IF NOT EXIST ".venv" (
    python -m venv .venv
    echo Ambiente virtual criado
)

REM Ativa o ambiente virtual
call .venv\Scripts\activate.bat

REM Instala o pacote localmente de forma editável
pip install --upgrade pip
pip install -e .

task


REM Mantém o terminal aberto
pause
