# Advanced Analytics: Dr. Semmelweis Handwashing Discovery

A data analytics project exploring the historical discovery of handwashing's impact on patient mortality, using Python with pandas, visualization libraries, and Jupyter notebooks.

## Overview

This project recreates Dr. Ignaz Semmelweis's groundbreaking 19th-century discovery about the importance of hand hygiene in preventing hospital-acquired infections. It uses data analysis techniques to demonstrate how simple handwashing protocols dramatically reduced mortality rates in Vienna General Hospital's maternity clinics.

## The Historical Context

In 1847, Dr. Semmelweis discovered that doctors washing their hands with chlorine solution (after performing autopsies) dramatically reduced the death rate among mothers in childbirth. This was decades before germ theory was established, making his discovery revolutionary.

## Project Structure

```
Part - Project 80 advance analitics/
├── Dr_Semmelweis_Handwashing_Discovery_(start).ipynb  Main Jupyter notebook
├── annual_deaths_by_clinic.csv                         Yearly death statistics
├── monthly_deaths.csv                                  Monthly death records
├── requirements.txt                                    Python dependencies
├── verificar_entorno.py                                Environment verification script
├── READme.txt                                          Original setup instructions
├── .vscode/                                            VS Code configuration
├── venv/                                               Virtual environment
├── .venv/                                              Alternative virtual environment
└── __MACOSX/                                           macOS metadata
```

## Data Files

### annual_deaths_by_clinic.csv
Contains yearly death statistics for two clinics at Vienna General Hospital:
- **Clinic 1**: Doctors' clinic (where handwashing was later mandated)
- **Clinic 2**: Midwives' clinic (control group)

### monthly_deaths.csv
More granular monthly data allowing for trend analysis over time.

## Tech Stack

- **Programming Language**: Python
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Notebook**: Jupyter (via ipykernel)
- **Statistics**: scipy

## Installation & Setup

### First-Time Setup (PowerShell)

1. **Navigate to project folder**:
   ```powershell
   cd "Part - Project 80 advance analitics"
   ```

2. **Create virtual environment** (if not exists):
   ```powershell
   python -m venv venv
   ```

3. **Install dependencies**:
   ```powershell
   .\venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

4. **Install Jupyter kernel**:
   ```powershell
   .\venv\Scripts\python.exe -m ipykernel install --user --name=semmelweis-day80 --display-name="Python (dia 80 Semmelweis)"
   ```

### Running the Notebook

1. **Open the notebook** in VS Code or Jupyter:
   ```
   Dr_Semmelweis_Handwashing_Discovery_(start).ipynb
   ```

2. **Select the correct kernel**:
   - Top-right of notebook → Select Kernel
   - Choose: `Python (dia 80 Semmelweis)`
   - Do NOT use generic Python kernels

3. **Run the SETUP cell first** to verify packages are installed

4. **Restart kernel** and run all cells

### Alternative: Verify Environment

```powershell
.\venv\Scripts\python.exe verificar_entorno.py
```

Expected output: OK for all packages, plus data shapes for both CSV files.

## What the Analysis Demonstrates

### Key Findings

1. **Before Handwashing (1840-1846)**:
   - Clinic 1 (Doctors): ~10-20% mortality rate
   - Clinic 2 (Midwives): ~2-3% mortality rate

2. **After Handwashing (1847-1849)**:
   - Clinic 1: Dropped to ~1-2% mortality rate
   - Dramatic reduction proves handwashing efficacy

### Analysis Techniques

- **Time Series Analysis**: Tracking mortality over months/years
- **Comparative Analysis**: Comparing two clinics
- **Statistical Significance**: Using scipy for hypothesis testing
- **Data Visualization**: Creating informative charts and graphs

## Notebook Sections (Typical)

1. **Setup Cell**: Package import and verification
2. **Data Loading**: Reading CSV files into pandas DataFrames
3. **Exploratory Data Analysis**: Initial data inspection
4. **Visualization**: Creating charts showing mortality trends
5. **Statistical Analysis**: Calculating significance of findings
6. **Conclusions**: Summarizing the discovery's impact

## Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
scipy
ipykernel
```

## Troubleshooting

### "No module named 'pandas'"
The notebook is using a kernel without required packages. Ensure you're using the `Python (dia 80 Semmelweis)` kernel.

### Kernel not appearing
Close and reopen the notebook after installing the kernel:
```powershell
.\venv\Scripts\python.exe -m ipykernel install --user --name=semmelweis-day80 --display-name="Python (dia 80 Semmelweis)"
```

### Import errors in notebook
Run the SETUP cell at the top of the notebook - it checks for missing packages and installs them if needed.

## Educational Value

This project demonstrates:
- How data analysis can reveal hidden patterns
- The importance of controlled experiments
- Statistical thinking in historical context
- Data visualization best practices
- Reproducible research workflows

## Historical Significance

Dr. Semmelweis's discovery was initially rejected by the medical establishment. It wasn't until Louis Pasteur developed germ theory decades later that his findings were fully accepted. Today, hand hygiene remains one of the most important infection control measures in healthcare.

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)