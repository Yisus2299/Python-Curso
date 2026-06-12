# Project 10 — Calculator

## Overview

An interactive calculator that supports chained operations using functions stored in a dictionary.

## What Was Built

A console calculator that performs addition, subtraction, multiplication, and division. Results can be reused in subsequent operations through recursive calls.

## Concepts Covered

- Functions as dictionary values
- `return` statements
- Recursion for chaining calculations
- User-driven flow control

## Files

| File | Description |
|------|-------------|
| `project_10_Calculator.py` | Main calculator |
| `part10_functions_outputs.py` | Practice on return values and docstrings |

## How to Run

```bash
python project_10_Calculator.py
```

## How It Works

1. The user picks an operation (`+`, `-`, `*`, `/`) and enters two numbers.
2. The result is displayed.
3. If the user chooses "yes", the result becomes the first operand for the next operation.
4. Choosing "no" restarts the calculator with a fresh call to `calculate()`.

## Requirements

- Python 3.x (standard library only)
