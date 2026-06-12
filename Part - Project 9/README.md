# Project 9 — Secret Auction

## Overview

A console-based blind auction where multiple bidders submit offers and the highest bid wins.

## What Was Built

An auction simulator that collects bidder names and amounts, clears the screen between entries, and declares the winner with the highest bid.

## Concepts Covered

- Dictionaries for storing bids
- Loops for collecting multiple entries
- Finding maximum values in a dictionary
- Screen clearing with escape sequences

## Files

| File | Description |
|------|-------------|
| `project_9_Subastas.py` | Main auction program |
| `part9_Dictionaries_Nesting.py` | Practice notes on dictionaries and nesting |

## How to Run

```bash
python project_9_Subastas.py
```

## How It Works

1. The program asks if there are other bidders.
2. Each bidder enters their name and bid amount (stored in a dictionary).
3. The screen is cleared between bidders for privacy.
4. When bidding ends, `winner_bet()` finds and displays the highest bidder.

## Requirements

- Python 3.x (standard library only)
