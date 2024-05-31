@echo off
setlocal

:: Crear el archivo main.py (sobrescribir si existe)
echo Creando main.py...
echo from modules.windows_principal import main > main.py
echo. >> main.py
echo if __name__ == "__main__": >> main.py
echo     main() >> main.py

:: Crear la carpeta modules (crear si no existe)
echo Creando la carpeta modules...
mkdir modules 2>nul

:: Crear el archivo __init__.py en la carpeta modules (sobrescribir si existe)
echo Creando __init__.py en la carpeta modules...
echo. > modules\__init__.py

:: Crear el archivo windows_principal.py en la carpeta modules (sobrescribir si existe)
echo Creando windows_principal.py en la carpeta modules...
echo import tkinter as tk > modules\windows_principal.py
echo. >> modules\windows_principal.py
echo def main(): >> modules\windows_principal.py
echo     root = tk.Tk() >> modules\windows_principal.py
echo     root.title("Mi Proyecto Tkinter") >> modules\windows_principal.py
echo     root.geometry("800x600") >> modules\windows_principal.py
echo. >> modules\windows_principal.py
echo     lbl = tk.Label(root, text="¡Hola, Mundo!") >> modules\windows_principal.py
echo     lbl.pack(pady=20) >> modules\windows_principal.py
echo. >> modules\windows_principal.py
echo     root.mainloop() >> modules\windows_principal.py

echo Estructura del proyecto creada exitosamente.
endlocal
pause
