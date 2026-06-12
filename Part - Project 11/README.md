# Project 11 — Blackjack

## Overview

A simplified console version of the card game Blackjack (21).

## What Was Built

A playable Blackjack game where the user receives cards, decides to hit or stand, and competes against a dealer who draws until reaching 17.

## Concepts Covered

- Modular functions (`deal_card`, `calculate_score`, `compare`)
- List manipulation for hands
- Ace handling (11 downgraded to 1 when needed)
- Game loop with replay option

## Files

| File | Description |
|------|-------------|
| `project_11_blackjack.py` | Main entry point |

## How to Run

```bash
python project_11_blackjack.py
```

## How It Works

1. The player and dealer each receive two cards.
2. The player chooses "hit" for another card or "stand" to hold.
3. `calculate_score()` totals hand values (Blackjack = 21, Aces = 11 or 1).
4. The dealer draws until score ≥ 17.
5. `compare()` determines the winner; the user can play again.

## Requirements

- Python 3.x (standard library only)
