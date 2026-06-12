# Project 8 — Caesar Cipher

## Overview

An interactive Caesar cipher tool that encodes and decodes text by shifting letters in the alphabet.

## What Was Built

A console program that lets the user encode or decode messages using a configurable shift value, with the option to run multiple operations in a loop.

## Concepts Covered

- Functions and `return` values
- `while` loops for repeated use
- Modulo arithmetic for alphabet wrapping
- Character encoding and decoding

## Files

| File | Description |
|------|-------------|
| `project_8_caesar cypher.py` | Main cipher program |
| `part8.py` | Practice exercises on functions |

## How to Run

```bash
python "project_8_caesar cypher.py"
```

## How It Works

1. The user chooses to encode or decode.
2. They enter a message and a shift number.
3. The `caesar()` function shifts each letter by the given amount.
4. The program asks whether to continue or exit.

## Requirements

- Python 3.x (standard library only)
