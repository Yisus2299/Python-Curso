# Project 28 — Pomodoro Timer (Tkinter)

## Overview

A Pomodoro Technique timer with a graphical interface, work/break cycles, and session tracking.

## What Was Built

A desktop Pomodoro timer that alternates between work sessions (25 min), short breaks (5 min), and long breaks (20 min every 8 cycles). Includes start, reset controls, and checkmark session markers.

## Concepts Covered

- Tkinter GUI (`Canvas`, `Label`, `Button`, `PhotoImage`)
- `window.after()` for countdown timers
- Global timer state management
- `pathlib` for asset paths

## Files

| File | Description |
|------|-------------|
| `mian.py` | Main entry point (note: filename typo) |
| `tomato.png` | Timer background image |

## How to Run

```bash
python mian.py
```

## How It Works

1. Click **Start** to begin a 25-minute work session.
2. When the timer reaches zero, a short break (5 min) begins automatically.
3. After every 8 work cycles, a long break (20 min) is triggered.
4. Checkmarks (✔) appear on the canvas after each completed work block.
5. **Reset** cancels the current timer and returns to the default state.

## Timer Cycles

| Phase | Duration |
|-------|----------|
| Work | 25 minutes |
| Short break | 5 minutes |
| Long break | 20 minutes (every 8 work sessions) |

## Requirements

- Python 3.x with Tkinter (standard library)
- `tomato.png` in the project folder
- A graphical environment (windowed display required)
