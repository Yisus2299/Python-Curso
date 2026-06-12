# Project 12 — Number Guessing Game

## Overview

A number guessing game where the player tries to find a secret number between 1 and 100.

## What Was Built

An interactive guessing game with two difficulty levels: Easy (10 attempts) and Hard (5 attempts). The program gives "Too high" or "Too low" hints after each guess.

## Concepts Covered

- Constants and functions
- `random.randint()` for secret numbers
- Difficulty-based attempt limits
- Global vs local scope (practice file)

## Files

| File | Description |
|------|-------------|
| `project_12_NumberGuessing.py` | Main game |
| `part12_Scopes_global.py` | Practice on variable scope and related exercises |

## How to Run

```bash
python project_12_NumberGuessing.py
```

## How It Works

1. A random number between 1 and 100 is generated.
2. The player selects Easy or Hard mode.
3. They guess until they find the number or run out of attempts.
4. Feedback guides each guess toward the correct answer.

## Requirements

- Python 3.x (standard library only)
