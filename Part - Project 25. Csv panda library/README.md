# Project 25 — CSV and Pandas Library Practice

## Overview

Hands-on exercises for reading, filtering, and manipulating CSV data with the Pandas library.

## What Was Built

Two scripts that explore Pandas fundamentals: one works with weather data (columns, rows, filtering, temperature conversion), and another analyzes squirrel census data from Central Park.

## Concepts Covered

- `pandas.read_csv()` and DataFrame operations
- Column/row selection and filtering
- Temperature conversion (Celsius to Fahrenheit)
- Creating CSV files from dictionaries
- Data aggregation and counting

## Files

| File | Description |
|------|-------------|
| `main.py` | Weather data tutorial and exercises |
| `squirelPractice.py` | Squirrel census analysis |
| `weather_data.csv` | Sample weather dataset |
| `2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv` | Squirrel census data |
| `new_data.csv` / `squirel_count.csv` | Generated output files |

## How to Run

```bash
python main.py
python squirelPractice.py
```

## How It Works

**`main.py`:**
1. Loads weather data from CSV.
2. Explores columns, rows, and conditional filtering.
3. Converts temperatures and creates new CSV output.

**`squirelPractice.py`:**
1. Reads the Central Park squirrel census dataset.
2. Counts squirrels by fur color.
3. Exports the summary to `squirel_count.csv`.

## Requirements

- Python 3.x
- `pandas` (`pip install pandas`)
