# Project 19 — Turtle Race

## Overview

A betting game where colored turtles race across the screen and the player wagers on the winner.

## What Was Built

An animated Turtle race with multiple turtles of different colors. The user picks a color to bet on, and turtles advance by random steps until one crosses the finish line.

## Concepts Covered

- Turtle graphics and multiple `Turtle` instances
- `Screen.textinput()` for user bets
- Lists of turtle objects
- Random movement in a game loop

## Files

| File | Description |
|------|-------------|
| `part19_POO_TurtleRaces.py` | Main entry point |

## How to Run

```bash
python part19_POO_TurtleRaces.py
```

## How It Works

1. Several turtles are created with distinct colors and starting positions.
2. The user enters a bet on which color will win.
3. Each round, all turtles move forward a random distance.
4. The first turtle to cross the finish line wins; the program announces whether the bet was correct.

## Requirements

- Python 3.x with Turtle (standard library)
- A graphical environment (windowed display required)
