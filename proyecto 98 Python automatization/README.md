# Organize Downloads

Qué hace:
- Ordena la carpeta `Downloads` por categoría (Imágenes, Videos, Documentos, Audio, Archivos, Instaladores, Código, Others).
- Dentro de cada categoría crea subcarpetas por fecha `YYYY-MM-DD` (usa fecha de modificación por defecto).
- Ignora archivos temporales (.crdownload, .part, .tmp, .partial).
- Renombra duplicados añadiendo " (n)".
- Modo one-shot y modo monitor en tiempo real.

Archivos
- `organize_downloads.py` : script principal.
- `requirements.txt` : dependencias opcionales (watchdog).

Requisitos
- Python 3.8+ (recomiendo 3.10+).
- (Opcional) `pip install -r requirements.txt` para usar `--watch`.

Uso
- Ejecutar una vez (auto-detecta Downloads):
  ```powershell
  python organize_downloads.py
  ```
- Ejecutar sobre ruta concreta:
  ```powershell
  python organize_downloads.py --path "C:\Users\TuUsuario\Downloads"
  ```
- Simular sin mover (recomendado para pruebas):
  ```powershell
  python organize_downloads.py --dry-run
  ```
- Modo monitor (requiere watchdog):
  ```powershell
  pip install -r requirements.txt
  python organize_downloads.py --watch
  ```
- Si `python` no funciona en PowerShell, usa el lanzador incluido:
  ```powershell
  .\run_organize_downloads.bat --dry-run
  .\run_organize_downloads.bat
  ```

Opciones útiles
- `--date-by mtime|ctime|now` : elegir fecha para carpetas.
- `--log <archivo>` : archivo de log (por defecto `organize_downloads.log`).

Notas de seguridad
- Revisa `organize_downloads.log` si algo no sale como esperas.
- Si quieres excluir tipos o carpetas, edita `DEFAULT_MAP` en el script.

Pruebas
- Haz primero `--dry-run` para ver acciones sin mover archivos.
