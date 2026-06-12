# Disappearing Writing App

A unique writing application that automatically deletes your text if you stop typing for a specified period. Inspired by the "Dangerous Writing" concept - a technique to encourage focused, stream-of-consciousness writing.

## Overview

This project implements a "dangerous writing" application where your work automatically disappears if you become inactive. The idea comes from the writing concept where the fear of losing work encourages continuous writing without overthinking or editing.

The project includes two implementations:
1. **Web Version**: Pure HTML/JavaScript
2. **Desktop Version**: Python Tkinter GUI

## Features

- **Auto-Delete**: Text is deleted after inactivity timeout
- **Configurable Timeout**: Choose between 5 or 10 seconds
- **Visual Feedback**: Status shows time remaining until deletion
- **Two Implementations**: Web and desktop versions

## Tech Stack

### Web Version
- HTML5
- JavaScript (vanilla)
- CSS3

### Desktop Version
- Python
- Tkinter (standard library)
- time module

## Project Structure

```
Part - Project 90 writting dissapearing app/
├── index.html     # Web version (HTML/CSS/JS)
└── mian.py        # Desktop version (Python/Tkinter)
```

---

# Web Version

## How to Use

1. Open `index.html` in any web browser
2. Select timeout duration (5 or 10 seconds)
3. Start typing in the text area
4. Keep typing - if you stop for the timeout duration, your text is deleted

## Implementation Details

### HTML Structure
- Dropdown selector for timeout (5 or 10 seconds)
- Textarea for writing
- Status div showing countdown message

### JavaScript Logic

```javascript
let timeout = 5;
let timerId = null;

function resetTimer() {
  clearTimeout(timerId);
  timeout = Number(sel.value);
  status.textContent = `Will delete after ${timeout}s of inactivity`;
  timerId = setTimeout(() => {
    if (editor.value.length) {
      editor.value = '';
      status.textContent = 'Deleted due to inactivity';
    }
  }, timeout * 1000);
}

editor.addEventListener('input', resetTimer);
sel.addEventListener('change', resetTimer);
```

### Event Listeners
- `input` event: Resets timer when user types
- `change` event: Updates timeout duration

---

# Desktop Version (Python/Tkinter)

## How to Run

```bash
python mian.py
```

## Application Components

### Main Window
- **Title**: "Dangerous Writer"
- **Size**: 800x500 pixels

### UI Elements

1. **Timeout Selector**: Dropdown to choose 5 or 10 seconds
2. **Status Label**: Shows countdown or message
3. **Text Area**: Main writing space with word wrap

### Code Architecture

```python
class App:
    def __init__(self):
        # Setup window, frames, widgets
        
    def on_key(self, event=None):
        # Reset timer on any key press
        
    def tick(self):
        # Check if timeout exceeded, delete text if needed
        # Update status label
        # Schedule next check (100ms)
```

### Key Functions

| Function | Description |
|----------|-------------|
| `set_timeout()` | Update global timeout variable |
| `on_key()` | Reset timer when user types |
| `tick()` | Check elapsed time, delete if needed |

### Timer Logic

```python
def tick():
    global last_activity
    remaining = timeout - (time.time() - last_activity)
    if remaining <= 0:
        content = text.get("1.0", "end-1c")
        if content:
            text.delete("1.0", "end")
            status.config(text="Deleted due to inactivity")
        last_activity = time.time()
    else:
        status.config(text=f"Delete in {remaining:.1f}s")
    root.after(100, tick)
```

---

# The Writing Concept

## Why "Dangerous Writing" Works

1. **Prevents Over-Editing**: Forces you to keep moving forward
2. **Encourages Flow State**: Similar to freewriting exercises
3. **Reduces Perfectionism**: Removes the urge to perfect as you go
4. **Builds Momentum**: Keeps you engaged in the writing process

## Tips for Using the App

1. **Don't Stop**: Keep your fingers moving
2. **Write Freely**: Don't worry about mistakes
3. **Embrace Chaos**: The deleted text was likely filler anyway
4. **Practice Daily**: Build your writing stamina

## Customization

### Web Version

**Change timeout options**:
```html
<select id="timeout">
  <option>5</option>
  <option>10</option>
  <option>15</option>  <!-- Add more options -->
</select>
```

**Change colors**:
```css
body { background: #f0f0f0; }
textarea { background: #ffffff; }
```

### Desktop Version

**Change default timeout**:
```python
var = tk.StringVar(value="10")  # Default to 10 seconds
```

**Change window size**:
```python
root.geometry("800x500")  # width x height
```

---

# Comparison

| Feature | Web Version | Desktop Version |
|---------|-------------|-----------------|
| Platform | Any browser | Python installed |
| UI | Simple HTML | Native desktop |
| Timeout options | 5, 10 seconds | 5, 10 seconds |
| Dependencies | None | Python stdlib |
| Ease of use | Open file | Run python script |

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)