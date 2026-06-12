# Project 26 — NATO Phonetic Alphabet Converter

## Overview

A console program that converts any word into its NATO phonetic alphabet equivalent using Pandas and comprehensions.

## What Was Built

A word-to-NATO converter that reads letter-to-code mappings from a CSV file, builds a lookup dictionary, and outputs the phonetic code for each letter in the user's input.

## Concepts Covered

- Pandas CSV reading
- Dictionary creation with `iterrows()` and comprehension
- List comprehension for output generation
- User input processing

## Files

| File | Description |
|------|-------------|
| `main.py` | Main entry point |
| `nato_phonetic_alphabet.csv` | Letter-to-NATO code mapping |

## How to Run

```bash
python main.py
```

## How It Works

1. The CSV file is loaded into a Pandas DataFrame.
2. A dictionary is built mapping each letter to its NATO phonetic code.
3. The user enters a word.
4. Each letter is converted to its NATO equivalent and printed as a list.

## Example

Input: `Hello`  
Output: `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`

## Requirements

- Python 3.x
- `pandas` (`pip install pandas`)
