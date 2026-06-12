# Police-Involved Deaths Analysis (U.S.)

This project analyzes datasets of police-involved deaths in the United States together with state-level socioeconomic indicators from the census.

## Expected files

- `fatal-police-shootings-data.csv` or `police_killings.csv`: police-involved deaths dataset.
- `us_census_data.csv` or `census_by_state.csv`: state-level census data including poverty rate, high school graduation rate, median household income, and racial demographics.

## Usage

1. Place the CSV files in the same folder as `main.py`.
2. Install dependencies if you don't have them:

```bash
pip install pandas matplotlib seaborn
```

3. Run the script:

```bash
python main.py
```

If `python` is not recognized in PowerShell, run with the full interpreter path, for example:

```powershell
& "C:/Users/ImKen/AppData/Local/Python/pythoncore-3.14-64/python.exe" main.py
```

Or set a temporary alias in that session:

```powershell
set-alias python "C:/Users/ImKen/AppData/Local/Python/pythoncore-3.14-64/python.exe"
python main.py
```

4. If your files have different names, specify them explicitly:

```bash
python main.py --shootings path/to/shootings.csv --census path/to/census.csv
```

5. Generated plots will be saved in the `analysis_output` directory.

## What the script does

- Loads and normalizes police-involved shootings and census datasets.
- Computes deaths per state.
- Merges the counts with socioeconomic indicators.
- Reports correlations between:
  - poverty rate
  - high school graduation rate
  - median household income
  - police-involved deaths per 100k
- Analyzes racial distribution of deaths.
- Produces scatter plots showing relationships between deaths per 100k and the main indicators.
