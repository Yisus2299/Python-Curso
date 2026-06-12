# Project 24 — File Paths and Reading Text Files

## Overview

A practice project for working with file paths using the `os` module and reading text files safely.

## What Was Built

A script that demonstrates three different ways to construct file paths (relative, user home directory, and absolute paths) and reads the contents of a text file using a context manager.

## Concepts Covered

- `os.path.join()` for cross-platform paths
- `os.path.dirname()` and `os.path.abspath()` for relative paths
- `os.path.expanduser("~")` for user home directory
- Raw strings and forward slashes for Windows paths
- `with open()` context manager and UTF-8 encoding

## Files

| File | Description |
|------|-------------|
| `parte24_automatizar.py` | Main script |
| `archivo.txt` | Sample text file to read |

## How to Run

```bash
python parte24_automatizar.py
```

## How It Works

1. The script defines multiple path constants pointing to `archivo.txt`:
   - Same folder as the script (relative path)
   - Desktop via `expanduser("~")`
   - Absolute path with raw string or forward slashes
2. It opens the file in read mode with UTF-8 encoding.
3. The full contents are read and printed to the console.

## Requirements

- Python 3.x (standard library only)
- `archivo.txt` must exist in the project folder or on the Desktop
