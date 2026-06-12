# Morse Code Converter

## Project Overview
A Python command-line application that converts text to Morse code using standard international Morse code mappings. This tool follows official Morse code standards and includes proper word and character separation.

## Technologies Used
- Python 3.x
- Standard library only (no external dependencies)
- Command-line interface
- String manipulation and mapping

## Project Structure
```
Part - Project 82 Morse Code Converter/
├── main.py              # Morse code converter application
└── README.md           # This file
```

## Features
- **Complete Morse Code Mapping**: Supports letters A-Z, numbers 0-9, and common punctuation
- **Proper Formatting**: Words separated by `/`, letters separated by spaces
- **Case Insensitive**: Automatically handles uppercase and lowercase input
- **Error Handling**: Gracefully handles unsupported characters
- **Clean Output**: Properly formatted Morse code output
- **Standards Compliance**: Follows international Morse code standards

## Installation
No installation required! This is a standalone Python script:
```bash
# Simply run the script
python main.py
```

## How to Use
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter text when prompted
3. View the Morse code conversion

### Example Usage
```
=== Morse Code Converter ===
Enter text: Hello World

Morse:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## Morse Code Standards
The converter uses the standard international Morse code as defined by the International Telecommunication Union (ITU).

### Character Mapping
```python
MORSE_CODE = {
    # Letters A-Z
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    
    # Numbers 0-9
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    
    # Punctuation and Symbols
    ".": ".-.-.-",      # Period
    ",": "--..--",      # Comma
    "?": "..--..",      # Question mark
    "'": ".----.",      # Apostrophe
    "!": "-.-.--",      # Exclamation mark
    "/": "-..-.",       # Slash
    "(": "-.--.",       # Left parenthesis
    ")": "-.--.-",      # Right parenthesis
    "&": ".-...",       # Ampersand
    ":": "---...",      # Colon
    ";": "-.-.-.",      # Semicolon
    "=": "-...-",       # Equals sign
    "+": ".-.-.",       # Plus sign
    "-": "-....-",      # Hyphen/minus
    "_": "..--.-",      # Underscore
    '"': ".-..-.",      # Quotation mark
    "$": "...-..-",     # Dollar sign
    "@": ".--.-.",      # At sign
}
```

## Code Explanation
### Main Conversion Function
```python
def text_to_morse(text: str) -> str:
    """Convert a text string to Morse code.
    
    Words are separated by a slash (/) and letters by spaces.
    Unknown characters are ignored.
    """
    words = []
    current_word = []
    
    for char in text:
        if char.isspace():
            if current_word:
                words.append(" ".join(current_word))
                current_word = []
            continue
        
        code = MORSE_CODE.get(char.upper())
        if code:
            current_word.append(code)
    
    if current_word:
        words.append(" ".join(current_word))
    
    return " / ".join(words)
```

### Main Application Loop
```python
def main():
    print("=== Morse Code Converter ===")
    user_text = input("Enter text: ")
    
    if not user_text.strip():
        print("No text entered.")
        return
    
    print("\nMorse:")
    print(text_to_morse(user_text))

if __name__ == "__main__":
    main()
```

## Morse Code Formatting Rules
### Character Separation
- **Letters**: Separated by single space
- **Words**: Separated by forward slash with spaces (` / `)
- **Example**: `HELLO WORLD` → `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

### Timing Standards (Reference)
- **Dot duration**: 1 unit
- **Dash duration**: 3 units
- **Intra-character space**: 1 unit (between dots/dashes)
- **Inter-character space**: 3 units (between letters)
- **Word space**: 7 units (between words)

## Extended Features
### Reverse Conversion (Morse to Text)
```python
def morse_to_text(morse: str) -> str:
    """Convert Morse code back to text."""
    # Create reverse mapping
    reverse_morse = {v: k for k, v in MORSE_CODE.items()}
    
    words = morse.split(" / ")
    text_words = []
    
    for word in words:
        letters = word.split()
        text_letters = []
        
        for letter in letters:
            if letter in reverse_morse:
                text_letters.append(reverse_morse[letter])
            else:
                text_letters.append("?")  # Unknown Morse code
        
        text_words.append("".join(text_letters))
    
    return " ".join(text_words)
```

### Audio Output (Optional Extension)
```python
import winsound  # Windows only
import time

def play_morse_code(morse_text: str, dot_duration: int = 100):
    """Play Morse code as audible tones."""
    dash_duration = dot_duration * 3
    frequency = 800  # Hz
    
    for char in morse_text:
        if char == '.':
            winsound.Beep(frequency, dot_duration)
        elif char == '-':
            winsound.Beep(frequency, dash_duration)
        elif char == ' ':
            time.sleep(dot_duration / 1000)  # Letter space
        elif char == '/':
            time.sleep(dot_duration * 7 / 1000)  # Word space
        time.sleep(dot_duration / 1000)  # Intra-character space
```

## Testing Examples
### Test Cases
```python
test_cases = [
    ("HELLO", ".... . .-.. .-.. ---"),
    ("WORLD", ".-- --- .-. .-.. -.."),
    ("HELLO WORLD", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
    ("123", ".---- ..--- ...--"),
    ("SOS", "... --- ..."),
    ("TEST 123", "- . ... - / .---- ..--- ...--"),
]
```

### Running Tests
```python
def run_tests():
    """Run conversion tests."""
    print("Running Morse code tests...")
    
    for text, expected in test_cases:
        result = text_to_morse(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} {text} -> {result}")
        
        if result != expected:
            print(f"  Expected: {expected}")
    
    print("\nAll tests completed.")
```

## Command Line Arguments
### Enhanced Version with Arguments
```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Morse Code Converter")
    parser.add_argument("text", nargs="?", help="Text to convert to Morse code")
    parser.add_argument("-r", "--reverse", action="store_true", 
                       help="Convert Morse code to text")
    parser.add_argument("-f", "--file", help="Read text from file")
    parser.add_argument("-o", "--output", help="Save output to file")
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read().strip()
    elif args.text:
        text = args.text
    else:
        text = input("Enter text: ")
    
    if args.reverse:
        result = morse_to_text(text)
        print(f"Text: {result}")
    else:
        result = text_to_morse(text)
        print(f"Morse: {result}")
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
```

## International Morse Code Variations
### Different Code Sets
```python
# American Morse Code (Railroad Morse)
AMERICAN_MORSE = {
    "A": ".-", "B": "-...", "C": ".. .", "D": "-..",
    # ... different mappings for some characters
}

# Gerke Code (Precursor to International Morse)
GERKE_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    # ... historical variations
}
```

## Educational Applications
### Learning Tool Features
```python
def practice_mode():
    """Interactive Morse code practice mode."""
    import random
    
    print("=== Morse Code Practice ===")
    print("Type 'quit' to exit")
    
    score = 0
    total = 0
    
    while True:
        # Generate random character
        char = random.choice(list(MORSE_CODE.keys())[:26])  # A-Z only
        
        print(f"\nCharacter: {char}")
        user_input = input("Morse code: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        correct = MORSE_CODE[char]
        
        if user_input == correct:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. Correct answer: {correct}")
        
        total += 1
    
    if total > 0:
        accuracy = (score / total) * 100
        print(f"\nFinal score: {score}/{total} ({accuracy:.1f}%)")
```

## Performance Considerations
### Optimization Techniques
```python
def optimized_text_to_morse(text: str) -> str:
    """Optimized version using list comprehensions."""
    # Pre-process: uppercase and split into words
    words = text.upper().split()
    
    # Convert each word
    morse_words = []
    for word in words:
        morse_letters = []
        for char in word:
            code = MORSE_CODE.get(char)
            if code:
                morse_letters.append(code)
        if morse_letters:
            morse_words.append(" ".join(morse_letters))
    
    return " / ".join(morse_words)
```

## Unicode Support
### Extended Character Set
```python
# Extended Morse code for international characters
EXTENDED_MORSE = {
    **MORSE_CODE,  # Standard characters
    
    # International characters
    "Ä": ".-.-",     # A with diaeresis
    "Á": ".--.-",    # A with acute
    "Å": ".--.-",    # A with ring
    "Ch": "----",    # Spanish Ch
    "É": "..-..",    # E with acute
    "Ñ": "--.--",    # N with tilde
    "Ö": "---.",     # O with diaeresis
    "Ü": "..--",     # U with diaeresis
    "ß": "...--..",  # German sharp S
}
```

## File I/O Operations
### Batch Processing
```python
def convert_file(input_file: str, output_file: str):
    """Convert entire text file to Morse code."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    morse_content = text_to_morse(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(morse_content)
    
    print(f"Converted {len(content)} characters")
```

## Project Purpose
This project demonstrates:
- String manipulation and mapping in Python
- Implementation of international standards
- Command-line application development
- Text processing algorithms
- Error handling and input validation
- Modular code organization
- Educational tool development
- Historical coding system implementation