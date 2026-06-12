# Flash Card App

## Project Overview
A language learning flash card application built with Python and Tkinter that helps users learn French vocabulary through interactive flash cards.

## Technologies Used
- Python 3.x
- Tkinter (GUI framework)
- Pandas (data manipulation)
- Pathlib (file path handling)

## Project Structure
```
Part - Project 31 Flash Card App/
├── main.py              # Main application file
├── data/
│   ├── french_words.csv # Original vocabulary data
│   └── words_to_learn.csv # User progress tracking
├── images/
│   ├── card_back.png    # Card back image
│   ├── card_front.png   # Card front image
│   ├── right.png        # Right button icon
│   └── wrong.png        # Wrong button icon
└── README.md            # This file
```

## Features
- Interactive flash card interface with flip animation
- Progress tracking (words marked as known are saved)
- Visual feedback with card flipping
- Persistent learning data across sessions
- Clean, user-friendly GUI design

## How to Run
1. Ensure Python 3.x is installed
2. Install required dependencies:
   ```
   pip install pandas
   ```
3. Run the application:
   ```
   python main.py
   ```

## Usage Instructions
1. Click the "❌" button if you don't know the word (it will appear again)
2. Click the "✅" button if you know the word (it will be removed from future sessions)
3. Cards automatically flip after 3 seconds to show the English translation
4. The app tracks your progress in `words_to_learn.csv`

## Configuration
- Modify `data/french_words.csv` to add/change vocabulary
- Update card images in the `images/` folder for customization
- Adjust flip timer duration in `main.py` (currently 3000ms)

## Project Purpose
This project demonstrates:
- GUI application development with Tkinter
- Data persistence with CSV files
- Object-oriented programming principles
- User progress tracking systems