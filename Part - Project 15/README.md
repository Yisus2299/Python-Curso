# Project 15 — Coffee Machine

## Overview

A console coffee machine simulator that sells drinks, tracks inventory, and collects coin payments.

## What Was Built

A functional coffee machine that offers espresso, latte, and cappuccino. It validates ingredient availability, processes coin input, gives change, and reports resources and profit.

## Concepts Covered

- Nested dictionaries for recipes and resources
- Global profit tracking
- Resource and payment validation
- Menu-driven console interface

## Files

| File | Description |
|------|-------------|
| `project_15_cafe_machine.py` | Main entry point |

## How to Run

```bash
python project_15_cafe_machine.py
```

## How It Works

1. The user selects a drink or enters `report` / `off`.
2. The machine checks if enough water, milk, and coffee are available.
3. The user inserts quarters, dimes, nickels, and pennies.
4. On successful payment, change is returned and ingredients are deducted.
5. `report` shows remaining resources and total profit.

## Requirements

- Python 3.x (standard library only)
