# Project 17 — Quiz Game (OOP)

## Overview

A True/False quiz game built with Object-Oriented Programming and a separated data/logic/UI structure.

## What Was Built

A console quiz that loads questions from a data module, wraps each in a `Question` object, and uses a `QuizBrain` class to ask questions, validate answers, and track the score.

## Concepts Covered

- OOP with model and logic classes
- Data separation (`data.py`)
- Class instantiation from lists
- Score tracking through object state

## Files

| File | Description |
|------|-------------|
| `proyecto17_POO_game.py` | Main entry point |
| `question_model.py` | `Question` class |
| `quiz_brain.py` | `QuizBrain` class — game logic |
| `data.py` | Question bank (text and answer) |
| `part17_POO_setting_all_up.py` | OOP setup practice (slices) |

## How to Run

```bash
python proyecto17_POO_game.py
```

## How It Works

1. Questions from `data.py` are converted into `Question` objects.
2. A `QuizBrain` instance asks each question in sequence.
3. The user answers True or False.
4. Correct answers increment the score; results are shown at the end.

## Requirements

- Python 3.x (standard library only)
