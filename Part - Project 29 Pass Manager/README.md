# Project 29 — Password Manager

## Overview

A GUI password manager that stores credentials in JSON, searches by website, and generates random passwords.

## What Was Built

A Tkinter desktop app for saving website/email/password combinations, searching stored entries, and generating secure random passwords copied to the clipboard.

## Concepts Covered

- Tkinter GUI design
- JSON file read/write for persistent storage
- `pyperclip` for clipboard integration
- `pathlib` for reliable file paths
- Random password generation with letters, numbers, and symbols

## Files

| File | Description |
|------|-------------|
| `main.py` | Main entry point |
| `data.json` | Stored credentials (website → email/password) |
| `logo.png` | Application logo |

## How to Run

```bash
pip install pyperclip
python main.py
```

## How It Works

1. **Add:** Enter a website, email/username, and password, then click Add to save to `data.json`.
2. **Search:** Enter a website name and click Search to retrieve the stored email and password.
3. **Generate Password:** Creates a random 8–10 character password with letters, numbers, and symbols, inserts it into the field, and copies it to the clipboard.

## Requirements

- Python 3.x with Tkinter (standard library)
- `pyperclip` (`pip install pyperclip`)
- A graphical environment (windowed display required)
