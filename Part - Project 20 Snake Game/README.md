# Project 20 — Snake Game

## Overview

A classic Snake game built with Python Turtle, featuring score tracking and persistent high scores.

## What Was Built

A fully playable Snake game where the snake grows by eating food, the score increases, and the highest score is saved to a file between sessions.

## Concepts Covered

- OOP with Turtle inheritance
- Collision detection (walls, tail, food)
- `Screen.tracer(0)` for smooth animation
- File I/O for high score persistence

## Files

| File | Description |
|------|-------------|
| `parte20_SnapeGame_partes.py` | Main game loop |
| `serpiente.py` | `Snake` class — movement and growth |
| `food.py` | `Food` class — random food placement |
| `puntaje.py` | `Scoreboard` class — score and high score |
| `data.txt` | High score storage |

## How to Run

```bash
python parte20_SnapeGame_partes.py
```

## How It Works

1. The snake moves continuously using W/A/S/D key bindings.
2. Eating food increases the score and adds a new body segment.
3. Colliding with a wall or the tail triggers game over and resets the snake.
4. The scoreboard updates the display and writes the high score to `data.txt`.

## Controls

| Key | Action |
|-----|--------|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |

## Requirements

- Python 3.x with Turtle (standard library)
- A graphical environment (windowed display required)
