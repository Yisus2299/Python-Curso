# REST API Practice with Pixela

## Project Overview
A hands-on project demonstrating CRUD (Create, Read, Update, Delete) operations using the Pixela API. This project creates and manages pixel-based graphs for habit tracking and data visualization.

## Technologies Used
- Python 3.x
- Requests library (HTTP client)
- Pixela API (pixel-based graphing service)
- datetime module
- JSON data handling

## Project Structure
```
Part - Project 37 POST PUT DELETE/
├── main.py              # Pixela API implementation
└── README.md           # This file
```

## Features
- User creation and management on Pixela
- Graph creation with customizable parameters
- Pixel data management (add, update, delete)
- HTTP methods practice: POST, GET, PUT, DELETE
- Date-based data tracking
- Graph visualization through web interface

## What is Pixela?
Pixela is a pixel-based graphing service that allows users to:
- Create custom graphs
- Track habits, moods, or any quantifiable data
- Visualize progress over time
- Share graphs publicly or keep them private

## Prerequisites
1. Pixela account (created through API)
2. Python 3.x installed
3. Requests library installed

## Installation
```
pip install requests
```

## How to Run
1. Configure your username and token in the script:
   ```python
   USERNAME = "your-username"
   TOKEN = "your-secret-token"
   ```

2. Run the script:
   ```
   python main.py
   ```

## API Endpoints Used

### 1. Create User (POST)
```python
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
requests.post("https://pixe.la/v1/users", json=user_params)
```

### 2. Create Graph (POST)
```python
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}
requests.post(f"{PIXELA_BASE}/{USERNAME}/graphs", json=graph_config, headers=headers)
```

### 3. Create Pixel (POST)
```python
pixel_data = {
    "date": "20260417",  # YYYYMMDD format
    "quantity": "30",    # Data value
}
requests.post(f"{PIXELA_BASE}/{USERNAME}/graphs/graph1", json=pixel_data, headers=headers)
```

### 4. Update Pixel (PUT)
```python
update_data = {"quantity": "45"}
requests.put(f"{PIXELA_BASE}/{USERNAME}/graphs/graph1/20260417", json=update_data, headers=headers)
```

### 5. Delete Pixel (DELETE)
```python
requests.delete(f"{PIXELA_BASE}/{USERNAME}/graphs/graph1/20260417", headers=headers)
```

## Graph Configuration Options

### Graph Types
- `int`: Integer values
- `float`: Decimal values

### Color Options
- `shibafu` (green)
- `momiji` (red)
- `sora` (blue)
- `ichou` (yellow)
- `ajisai` (purple)
- `kuro` (black)

### Unit Examples
- `minutes`, `hours`, `pages`
- `cups`, `glasses`, `times`
- Custom units like `pushups`, `words`, `km`

## Viewing Your Graph
Once created, view your graph at:
```
https://pixe.la/v1/{USERNAME}/graphs/{GRAPH_ID}.html
```

Example:
```
https://pixe.la/v1/jesus-imken-20260417/graphs/graph1.html
```

## Date Format
Pixela uses `YYYYMMDD` format for dates:
- `20260417` = April 17, 2026
- `20251225` = December 25, 2025

## Error Handling
- HTTP status code checking
- JSON response validation
- Network timeout management
- Authentication error handling
- Invalid date format validation

## Example Use Cases
1. **Habit Tracking**: Reading minutes per day
2. **Exercise Log**: Pushups or workout duration
3. **Mood Tracking**: Daily happiness score (1-10)
4. **Water Intake**: Glasses of water per day
5. **Study Time**: Hours of study per subject

## Project Purpose
This project demonstrates:
- RESTful API consumption
- HTTP methods (POST, GET, PUT, DELETE)
- API authentication with tokens
- Date-based data management
- Graph creation and visualization
- Habit tracking system design