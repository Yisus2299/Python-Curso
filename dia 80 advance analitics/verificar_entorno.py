"""Run:  venv\\Scripts\\python.exe verificar_entorno.py"""
import sys

print("Python:", sys.executable)

errors = []
for pkg in ("pandas", "numpy", "plotly", "seaborn", "matplotlib", "scipy"):
    try:
        __import__(pkg)
        print(f"  OK  {pkg}")
    except ImportError as e:
        print(f"  FAIL {pkg}: {e}")
        errors.append(pkg)

if errors:
    print("\nInstall with:")
    print(f'  "{sys.executable}" -m pip install -r requirements.txt')
    sys.exit(1)

import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parent
df_y = pd.read_csv(base / "annual_deaths_by_clinic.csv")
df_m = pd.read_csv(base / "monthly_deaths.csv", parse_dates=["date"])
print(f"\nData OK: yearly {df_y.shape}, monthly {df_m.shape}")
print("\nEnvironment ready. In Cursor select kernel: Python (dia 80 Semmelweis)")
