# Project 16 — Coffee Machine (OOP)

## Overview

An object-oriented refactor of the coffee machine project, splitting responsibilities into dedicated classes.

## What Was Built

The same coffee machine functionality from Project 15, restructured using Object-Oriented Programming. Each component — menu, coffee maker, and payment — is encapsulated in its own class.

## Concepts Covered

- Object-Oriented Programming (OOP)
- Separation of concerns across classes
- Class attributes and methods
- Composition of objects in a main loop

## Files

| File | Description |
|------|-------------|
| `proyecto16_cafe_POO.py` | Main entry point |
| `menu.py` | `Menu` class — drink definitions and lookup |
| `coffee_maker.py` | `CoffeeMaker` class — resources and brewing |
| `money_machine.py` | `MoneyMachine` class — coin payment and profit |
| `main.py` | Module imports (no game loop) |
| `Part16_POO_libraries.py` | OOP library practice notes |

## How to Run

```bash
python proyecto16_cafe_POO.py
```

## How It Works

1. `Menu` provides available drinks and their recipes.
2. `CoffeeMaker` checks ingredient levels and prepares drinks.
3. `MoneyMachine` handles coin insertion, change, and profit reporting.
4. The main loop in `proyecto16_cafe_POO.py` ties all classes together via user input.

## Requirements

- Python 3.x (standard library only)
