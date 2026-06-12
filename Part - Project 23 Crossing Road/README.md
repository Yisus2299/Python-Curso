# Project 23 — Crossing Road (Frogger)

## Overview

A Frogger-style game where the player crosses a busy road while avoiding moving cars.

## What Was Built

A Turtle-based arcade game with a player character, randomly spawned cars, increasing difficulty levels, and a scoreboard that tracks progress.

## Concepts Covered

- OOP with dedicated classes for player, cars, and score
- Random car spawning and movement
- Collision detection
- Progressive difficulty (speed increases per level)

## Files

| File | Description |
|------|-------------|
| `main.py` | Main game loop |
| `player.py` | `Player` class — movement |
| `car_manager.py` | `CarManager` class — car creation and movement |
| `scoreboard.py` | `Scoreboard` class — level and score display |

## How to Run

```bash
python main.py
```

## How It Works

1. The player starts at the bottom and moves upward with the W key.
2. Cars spawn at random intervals and move across the screen.
3. Reaching the top increases the level and car speed.
4. Colliding with a car triggers GAME OVER.

## Controls

| Key | Action |
|-----|--------|
| W | Move up |

## Requirements

- Python 3.x with Turtle (standard library)
- A graphical environment (windowed display required)
