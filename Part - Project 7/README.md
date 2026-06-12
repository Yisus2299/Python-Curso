# Project 7 — Hangman

## Overview

A classic Hangman word-guessing game played in the terminal.

## What Was Built

A console Hangman game that picks a random word, lets the player guess letters one at a time, and tracks lives until the word is completed or the player runs out of attempts.

## Concepts Covered

- `while` loops
- Lists and strings
- Placeholder display with underscores
- Life counter logic

## Files

| File | Description |
|------|-------------|
| `project_7_hangman.py` | Main entry point |

## How to Run

```bash
python project_7_hangman.py
```

## How It Works

1. A random word is selected from a predefined list.
2. The player guesses one letter at a time.
3. Correct guesses reveal letters; wrong guesses reduce lives (6 total).
4. The game ends on a win (word complete) or loss (no lives left).

## Requirements

- Python 3.x (standard library only)
