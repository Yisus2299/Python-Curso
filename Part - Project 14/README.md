# Project 14 — Higher or Lower

## Overview

A trivia game where the player compares follower counts of famous social media accounts.

## What Was Built

A score-based game that displays two celebrity or brand accounts and asks whether the second has more followers than the first. Correct guesses increase the score and continue the streak.

## Concepts Covered

- Lists of dictionaries for game data
- `random.choice()` for account selection
- Score tracking across rounds
- Conditional game-over logic

## Files

| File | Description |
|------|-------------|
| `part14__Higher_or_Lower_Project_basic.py` | Main entry point |

## How to Run

```bash
python part14__Higher_or_Lower_Project_basic.py
```

## How It Works

1. Two accounts are shown with one follower count visible.
2. The player guesses whether the hidden account (A or B) has more followers.
3. A correct answer adds a point and presents a new pair.
4. A wrong answer ends the game and displays the final score.

## Requirements

- Python 3.x (standard library only)
