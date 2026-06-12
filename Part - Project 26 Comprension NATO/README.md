# Project 26 — List and Dictionary Comprehensions (NATO)

## Overview

Practice exercises for Python comprehensions and Pandas iteration, using NATO alphabet and file data as examples.

## What Was Built

Three independent practice scripts covering list comprehensions, dictionary comprehensions, and iterating over Pandas DataFrames.

## Concepts Covered

- List comprehensions with and without conditions
- Dictionary comprehensions
- File reading and set intersection
- `DataFrame.iterrows()` for row-by-row processing
- Temperature data transformation

## Files

| File | Description |
|------|-------------|
| `list_comprehension.py` | List comprehension exercises and file intersection |
| `dictionaryComprehension.py` | Dictionary comprehension examples |
| `iteratePandas.py` | Pandas row iteration practice |
| `file1.txt` / `file2.txt` | Sample text files for intersection exercise |

## How to Run

```bash
python list_comprehension.py
python dictionaryComprehension.py
python iteratePandas.py
```

## How It Works

- **`list_comprehension.py`:** Transforms lists using comprehensions; finds common words between two text files.
- **`dictionaryComprehension.py`:** Builds dictionaries from existing data using comprehension syntax.
- **`iteratePandas.py`:** Loops through DataFrame rows to process or transform data.

## Requirements

- Python 3.x
- `pandas` for `iteratePandas.py` (`pip install pandas`)
