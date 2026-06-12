# Project 30 — Exceptions and JSON

## Overview

Practice with Python exception handling (`try/except/else/finally`) and a NATO phonetic alphabet app with input validation.

## What Was Built

Two scripts: a NATO converter that gracefully handles invalid characters using `KeyError`, and a standalone exceptions module demonstrating error handling patterns and custom `raise` statements.

## Concepts Covered

- `try` / `except` / `else` / `finally` blocks
- Handling `KeyError` for invalid input
- Recursive retry on error
- Custom exceptions with `raise ValueError`
- Pandas dictionary comprehension with `iterrows()`

## Files

| File | Description |
|------|-------------|
| `main.py` | NATO alphabet converter with exception handling |
| `exceptions.py` | Exception handling exercises and validation |
| `nato_phonetic_alphabet.csv` | Letter-to-NATO code mapping |
| `a_file.txt` | Sample file for file-handling exercises |
| `pyproject.toml` / `poetry.lock` | Poetry dependency configuration |

## How to Run

```bash
pip install pandas
python main.py
python exceptions.py
```

## How It Works

**`main.py`:**
1. Loads NATO phonetic codes from CSV into a dictionary.
2. Prompts the user for a word.
3. Converts each letter to its NATO code using list comprehension.
4. If a non-alphabetic character is entered, catches `KeyError`, prints an error message, and prompts again.

**`exceptions.py`:**
1. Demonstrates basic try/except patterns.
2. Includes a height validation function that raises `ValueError` if the value exceeds 3 meters.

## Requirements

- Python 3.x
- `pandas` for `main.py` (`pip install pandas`)
