DAY 80 - Dr Semmelweis Handwashing Discovery
=============================================

Project folder for the Advanced Analytics notebook on Dr Ignaz Semmelweis.

Files
-----
- Dr_Semmelweis_Handwashing_Discovery_(start).ipynb  Main notebook
- annual_deaths_by_clinic.csv                         Yearly clinic data
- monthly_deaths.csv                                  Monthly death records
- requirements.txt                                    Python dependencies
- verificar_entorno.py                                Environment + data check
- .vscode/settings.json                               Cursor/VS Code defaults

Problem
-------
Errors like "No module named 'pandas'" or "pd is not defined" mean the notebook
is using a Python kernel that does not have the required libraries installed.

What was set up
---------------
1. A project virtual environment (venv/) with pandas, numpy, plotly, seaborn,
   matplotlib, scipy, and ipykernel (see requirements.txt).

2. A dedicated Jupyter kernel:
   - Internal name: semmelweis-day80
   - Display name: Python (dia 80 Semmelweis)

3. VS Code / Cursor settings (.vscode/settings.json):
   - Default interpreter: venv/Scripts/python.exe
   - Default Jupyter kernel: semmelweis-day80

4. A SETUP cell at the top of the notebook that checks for missing packages
   and installs them into the active kernel if needed.

5. A verification script (verificar_entorno.py) that checks imports and loads
   both CSV files.

First-time setup (PowerShell, from this folder)
-----------------------------------------------
If venv/ does not exist yet:

  python -m venv venv
  .\venv\Scripts\python.exe -m pip install -r requirements.txt
  .\venv\Scripts\python.exe -m ipykernel install --user --name=semmelweis-day80 --display-name="Python (dia 80 Semmelweis)"

How to run the notebook in Cursor / VS Code
-------------------------------------------
1. Open this folder (or the .ipynb file).

2. Top-right of the notebook: Select Kernel
   -> Choose: Python (dia 80 Semmelweis)
   Do NOT use a generic ".venv" or unnamed "Python 3.x" kernel.

3. Run the first code cell (SETUP) to verify Python and install any missing packages.

4. Restart Kernel, then Run All (or run cells top to bottom).

If the correct kernel does not appear
---------------------------------------
Close and reopen the notebook after running:

  .\venv\Scripts\python.exe -m ipykernel install --user --name=semmelweis-day80 --display-name="Python (dia 80 Semmelweis)"

Verify environment (optional)
-------------------------------
  .\venv\Scripts\python.exe verificar_entorno.py

Expected output: OK for all packages, plus data shapes for both CSV files.
If anything fails, reinstall with:

  .\venv\Scripts\python.exe -m pip install -r requirements.txt