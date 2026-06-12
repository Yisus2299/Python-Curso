# Typing Speed Test Application

A desktop application built with Python's Tkinter library that measures typing speed (WPM) and accuracy through an interactive test.

## Overview

This project is a GUI-based typing speed test application that challenges users to type a given text as quickly and accurately as possible within a 60-second time limit. It calculates Words Per Minute (WPM) and accuracy percentage in real-time.

## Features

- **Timed Test**: 60-second countdown timer
- **Real-Time Stats**: Live WPM and accuracy updates
- **Performance Levels**: Feedback based on typing speed
- **Dark Theme**: Modern dark UI design
- **Start/Reset**: Control test execution
- **Accuracy Tracking**: Character-by-character comparison

## Tech Stack

- **GUI Framework**: Tkinter (Python standard library)
- **Time Tracking**: time module
- **Message Boxes**: tkinter.messagebox

## Project Structure

```
Part - Project 86 Tkinter Speed test/
└── speedTest.py    # Main application file
```

## How It Works

### Core Functionality

1. **Display sample text** for the user to type
2. **Start timer** when user clicks "Start"
3. **Track typing** character-by-character in real-time
4. **Calculate metrics** every 200ms
5. **End test** when time expires or user completes text

### WPM Calculation

```python
def calculate_wpm(self, typed, seconds):
    if seconds <= 0:
        return 0
    correct = self.correct_chars(self.target_text, typed)
    minutes = seconds / 60
    return int((correct / 5) / minutes)
```

WPM = (Correct characters / 5) / Minutes elapsed

### Accuracy Calculation

```python
def calculate_accuracy(self, typed):
    if not typed:
        return 0
    correct = self.correct_chars(self.target_text, typed)
    return int((correct / len(typed)) * 100)
```

### Performance Levels

| WPM | Level |
|-----|-------|
| < 40 | Below average |
| 40-59 | Average |
| 60-79 | Above average |
| 80-99 | Advanced |
| 100+ | Expert |

## Installation & Running

No additional dependencies required (uses Python standard library).

```bash
python speedTest.py
```

## Application Components

### Main Window
- **Size**: 700x400 pixels
- **Background**: Dark gray (#1E1E28)
- **Title**: "Typing Speed Test"

### UI Elements

1. **Instructions Label**: "Type the text below as quickly and accurately as you can:"
2. **Sample Text Display**: Shows the text to type (dark background, white text)
3. **Text Entry Area**: Multi-line text box for user input
4. **Status Bar**:
   - Timer display: "Time: XX s"
   - WPM display: "WPM: 0"
   - Accuracy display: "Accuracy: 0%"
5. **Control Buttons**:
   - Start: Begins the test
   - Reset: Clears and resets everything

## Code Architecture

### AppSpeedTest Class

```python
class AppSpeedTest:
    def __init__(self, root):
        # Initialize UI components
    
    def correct_chars(self, target, typed):
        # Count correct characters in order
    
    def calculate_wpm(self, typed, seconds):
        # Calculate words per minute
    
    def calculate_accuracy(self, typed):
        # Calculate accuracy percentage
    
    def start(self):
        # Start the test
    
    def reset(self, no_message=False):
        # Reset the test
    
    def tick(self):
        # Update timer and stats
    
    def on_type(self, event=None):
        # Handle typing events
    
    def finish(self):
        # End test and show results
```

### Key Methods

| Method | Description |
|--------|-------------|
| `__init__` | Initialize all UI components |
| `start` | Begin the test, enable text entry |
| `reset` | Clear text and reset all counters |
| `tick` | Update timer, WPM, accuracy (called every 200ms) |
| `finish` | End test, show final results dialog |

### Event Handling

- **Key Release**: Updates WPM and accuracy in real-time
- **Timer**: Counts down from 60 seconds
- **Completion**: Triggers when time expires or text fully typed

## Customization

### Changing Test Duration

Modify the `self.duration` value in `__init__`:
```python
self.duration = 60  # seconds
```

### Changing Sample Text

Update `SAMPLE_TEXT` at the top of the file:
```python
SAMPLE_TEXT = "Your custom text here..."
```

### Changing UI Colors

Modify `rgb_a_hex()` values or hardcoded colors:
```python
bg_color = rgb_a_hex(30, 30, 40)  # RGB values
```

## Color Helper

```python
def rgb_a_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
```

Converts RGB (0-255) to hex color codes for Tkinter.

## Example Output

```
WPM: 65
Accuracy: 92%

Above average. Very good.
```

## Tips for Testing

1. Click "Start" before typing begins the timer
2. The test automatically ends when you type the full text
3. Use "Reset" to try again
4. Focus on accuracy first, speed will follow

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)