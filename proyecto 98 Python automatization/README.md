# Organize Downloads

What it does:
- Organizes the `Downloads` folder into categories (Images, Videos, Documents, Audio, Archives, Installers, Code, Others).
- Creates date-based subfolders (`YYYY-MM-DD`) inside each category (uses modification time by default).
- Ignores temporary download files (.crdownload, .part, .tmp, .partial).
- Renames duplicates by appending " (n)".
- Supports one-shot run and real-time watch mode.

Files
- `organize_downloads.py`: main script.
- `requirements.txt`: optional dependencies (for `watchdog`).

Requirements
- Python 3.8+ (3.10+ recommended).
- (Optional) `pip install -r requirements.txt` to enable `--watch`.

Usage
- Run once (auto-detects Downloads):
  ```powershell
  python organize_downloads.py
  ```
- Run against a specific path:
  ```powershell
  python organize_downloads.py --path "C:\Users\YourUser\Downloads"
  ```
- Simulate without moving files (recommended for testing):
  ```powershell
  python organize_downloads.py --dry-run
  ```
- Watch mode (requires `watchdog`):
  ```powershell
  pip install -r requirements.txt
  python organize_downloads.py --watch
  ```
- If `python` is not available in PowerShell, use the bundled launcher:
  ```powershell
  .\run_organize_downloads.bat --dry-run
  .\run_organize_downloads.bat
  ```

Useful options
- `--date-by mtime|ctime|now`: choose which timestamp to use for folders.
- `--log <file>`: log file (default `organize_downloads.log`).

Security notes
- Review `organize_downloads.log` if anything unexpected happens.
- To exclude file types or folders, edit `DEFAULT_MAP` in the script.

Testing
- Use `--dry-run` first to preview actions without moving files.
