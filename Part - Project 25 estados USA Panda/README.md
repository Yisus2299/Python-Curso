# Project 25 — U.S. States Learning Game

## Overview

An educational Turtle game where the player learns U.S. state names by typing them on a blank map.

## What Was Built

An interactive map quiz that displays a blank U.S. map. When the user correctly names a state, its name is written at the correct coordinates. At the end, a CSV file is generated listing states the player still needs to learn.

## Concepts Covered

- Pandas for reading CSV data
- Turtle graphics for map display and text writing
- List comprehensions for filtering learned states
- `DataFrame.to_csv()` for exporting results

## Files

| File | Description |
|------|-------------|
| `main.py` | Main entry point |
| `50_states.csv` | State names and x/y coordinates |
| `blank_states_img.gif` | Blank U.S. map image |
| `states_to_learn.csv` | Generated file with missed states (created on exit) |

## How to Run

```bash
python main.py
```

## How It Works

1. A blank U.S. map is displayed using Turtle.
2. The user types state names in the input prompt.
3. Correct answers write the state name at its coordinates on the map.
4. On exit, states not guessed are saved to `states_to_learn.csv` for later study.

## Requirements

- Python 3.x
- `pandas` (`pip install pandas`)
- Turtle (standard library)
- A graphical environment (windowed display required)
