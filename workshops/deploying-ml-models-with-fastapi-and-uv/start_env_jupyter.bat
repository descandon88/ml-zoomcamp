
REM Activar el entorno virtual
call env\Scripts\activate.bat

IF ERRORLEVEL 1 (
    echo Error al activar el entorno virtual. ¿Seguro que fue creado?
    pause
    exit /b
)

echo Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

echo Iniciando Jupyter Notebook...
jupyter notebook