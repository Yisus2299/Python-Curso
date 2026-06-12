# Project 22 — Ping Pong

## Overview

A two-player Pong game built with Python Turtle graphics.

## What Was Built

A real-time Pong game with two paddles, a bouncing ball, and a scoreboard. Players control their paddles with keyboard input while the ball rebounds off walls and paddles.

## Concepts Covered

- OOP with separate classes for ball, paddles, and scoreboard
- `Screen.tracer()` for animation
- Collision detection
- Keyboard event listeners

## Files

| File | Description |
|------|-------------|
| `pong.py` | Main game loop |
| `ball.py` | `Ball` class — movement and bouncing |
| `paddles.py` | `Paddle` class — player controls |
| `scoreboard.py` | `Scoreboard` class — point tracking |

## How to Run

```bash
python pong.py
```

## How It Works

1. Two paddles are placed on opposite sides of the screen.
2. The ball moves and bounces off the top/bottom walls and paddles.
3. If the ball exits on the left or right, the opposing player scores.
4. The scoreboard updates after each point.

## Controls

| Player | Keys |
|--------|------|
| Left paddle | Up / Down arrows |
| Right paddle | W / S |

## Requirements

- Python 3.x with Turtle (standard library)
- A graphical environment (windowed display required)
