# Dinosaur Game Automation Bot

## Project Overview
An automation bot for the Chrome Dino game (chrome://dino) that uses computer vision and screen capture to detect obstacles and automatically jump over them. This project demonstrates game automation, screen interaction, and real-time image processing.

## Technologies Used
- Python 3.x
- PyAutoGUI (screen capture and input simulation)
- PIL/Pillow (image processing)
- Time module (delays and timing)
- Coordinate-based screen interaction
- Grayscale image analysis

## Project Structure
```
Part - Project 94 dinosaur python game/
├── game.py              # Main automation bot script
└── README.md           # This file
```

## Features
- **Automatic Obstacle Detection**: Uses screen capture to detect obstacles
- **Real-time Processing**: Continuously scans the game area
- **Configurable Parameters**: Adjustable detection thresholds and scan regions
- **Calibration System**: Manual calibration for different screen setups
- **Error Handling**: Graceful failure and recovery
- **Performance Optimization**: Efficient scanning algorithms
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation
### Prerequisites
1. Python 3.x installed
2. Install required packages:
   ```bash
   pip install pyautogui pillow
   ```

### Game Setup
1. Open the Chrome Dino game:
   - Chrome/Edge: Navigate to `chrome://dino`
   - Brave: Navigate to `brave://dino`
2. Ensure the game is visible on screen
3. Position the game window appropriately

## How to Use
1. Run the script:
   ```bash
   python game.py
   ```
2. Follow the calibration instructions:
   - Move mouse cursor over the dinosaur
   - Press Enter when ready
3. The bot will start in 3 seconds
4. Switch to the game window
5. Watch the bot play automatically

## Configuration Parameters
```python
# Detection threshold (0-255, lower = more sensitive)
THRESHOLD = 120

# Scan region dimensions (adjust based on game speed)
SCAN_WIDTH = 140    # Width of area to scan for obstacles
SCAN_HEIGHT = 30    # Height of area to scan

# Offset from dinosaur position
OFFSET_X = 80       # Horizontal offset to start scanning
OFFSET_Y = 10       # Vertical offset (negative = above dino)
```

## Code Structure
### Calibration Function
```python
def calibrate():
    """Calibrate the bot by finding the dinosaur's location."""
    print("Open chrome://dino and place the browser where the game is visible.")
    print("Move your mouse cursor over the dino and press Enter.")
    input("Press Enter when the mouse is over the dino...")
    
    # Get current mouse position (dinosaur location)
    x, y = pyautogui.position()
    
    # Define scan region relative to dinosaur
    region = (
        x + OFFSET_X,      # Start scanning to the right of dino
        y - OFFSET_Y,      # Start scanning above dino
        SCAN_WIDTH,        # Width to scan
        SCAN_HEIGHT        # Height to scan
    )
    
    print(f"Using scan region: {region}")
    return region
```

### Obstacle Detection
```python
def obstacle_ahead(region):
    """Check if there's an obstacle in the scan region."""
    # Capture screenshot of scan region
    screenshot = pyautogui.screenshot(region=region)
    
    # Convert to grayscale for faster processing
    gray = ImageOps.grayscale(screenshot)
    
    # Get pixel data
    pixels = gray.getdata()
    
    # Check for dark pixels (obstacles)
    return any(pixel < THRESHOLD for pixel in pixels)
```

### Jump Action
```python
def jump():
    """Simulate a jump by pressing the spacebar."""
    pyautogui.press("space")
```

### Main Game Loop
```python
def main():
    """Main bot execution loop."""
    # Calibrate scan region
    scan_region = calibrate()
    
    print("Bot will start in 3 seconds. Switch to the game window.")
    time.sleep(3)
    
    # Start the game if not already running
    pyautogui.press("space")
    time.sleep(0.5)
    
    # Main game loop
    while True:
        if obstacle_ahead(scan_region):
            jump()
            time.sleep(0.15)  # Cooldown between jumps
        
        # Small delay to prevent CPU overuse
        time.sleep(0.01)
```

## Advanced Features
### Dynamic Threshold Adjustment
```python
class AdaptiveThreshold:
    """Dynamically adjust detection threshold based on game state."""
    
    def __init__(self, initial_threshold=120):
        self.threshold = initial_threshold
        self.adjustment_rate = 5
        self.min_threshold = 80
        self.max_threshold = 180
    
    def adjust(self, jump_successful):
        """Adjust threshold based on jump success."""
        if jump_successful:
            # Increase threshold (be less sensitive) if jumps are working
            self.threshold = min(self.threshold + self.adjustment_rate, self.max_threshold)
        else:
            # Decrease threshold (be more sensitive) if missing obstacles
            self.threshold = max(self.threshold - self.adjustment_rate, self.min_threshold)
    
    def get_threshold(self):
        return self.threshold
```

### Multiple Obstacle Types
```python
def detect_obstacle_type(region):
    """Detect different types of obstacles (cacti vs birds)."""
    screenshot = pyautogui.screenshot(region=region)
    gray = ImageOps.grayscale(screenshot)
    
    # Analyze pixel distribution
    pixels = list(gray.getdata())
    dark_pixels = [p for p in pixels if p < THRESHOLD]
    
    if not dark_pixels:
        return None  # No obstacle
    
    # Calculate obstacle characteristics
    avg_brightness = sum(dark_pixels) / len(dark_pixels)
    height_variation = max(dark_pixels) - min(dark_pixels)
    
    # Classify based on characteristics
    if height_variation > 50:
        return "bird"  # Birds have more vertical variation
    else:
        return "cactus"  # Cacti are more uniform
```

### Game State Monitoring
```python
class GameStateMonitor:
    """Monitor game state and adjust bot behavior."""
    
    def __init__(self):
        self.score = 0
        self.speed = 1.0
        self.game_over = False
        self.last_check = time.time()
    
    def update(self):
        """Update game state based on screen analysis."""
        current_time = time.time()
        
        # Check for game over screen
        if self.check_game_over():
            self.game_over = True
            return
        
        # Estimate score based on time played
        if current_time - self.last_check > 1.0:  # Update every second
            self.score += 100  # Approximate score increase
            self.speed = min(10.0, 1.0 + (self.score / 10000))  # Speed increases with score
            self.last_check = current_time
    
    def check_game_over(self):
        """Check if game over screen is displayed."""
        # Capture screen area where game over text appears
        game_over_region = (400, 300, 200, 100)  # Adjust based on screen resolution
        screenshot = pyautogui.screenshot(region=game_over_region)
        
        # Simple color detection for game over text
        pixels = list(screenshot.getdata())
        white_pixels = [p for p in pixels if sum(p[:3]) > 600]  # Bright pixels
        
        return len(white_pixels) > 100  # If many bright pixels, likely game over
    
    def get_scan_parameters(self):
        """Get scan parameters based on current game speed."""
        base_width = 140
        base_height = 30
        
        # Adjust scan area based on speed
        adjusted_width = int(base_width * self.speed)
        adjusted_height = int(base_height * self.speed)
        
        return adjusted_width, adjusted_height
```

## Performance Optimization
### Efficient Scanning Algorithms
```python
def optimized_obstacle_ahead(region, sample_rate=5):
    """
    Optimized obstacle detection using sampling.
    
    Args:
        region: (x, y, width, height) tuple
        sample_rate: Check every Nth pixel (higher = faster)
    """
    screenshot = pyautogui.screenshot(region=region)
    gray = ImageOps.grayscale(screenshot)
    pixels = gray.getdata()
    
    # Sample pixels instead of checking every one
    for i in range(0, len(pixels), sample_rate):
        if pixels[i] < THRESHOLD:
            return True
    
    return False
```

### Caching and Preprocessing
```python
class ScreenCache:
    """Cache screen captures to reduce processing load."""
    
    def __init__(self, cache_duration=0.1):
        self.cache = None
        self.cache_time = 0
        self.cache_duration = cache_duration
    
    def get_screenshot(self, region):
        """Get screenshot, using cache if recent."""
        current_time = time.time()
        
        if (self.cache is None or 
            current_time - self.cache_time > self.cache_duration):
            # Update cache
            self.cache = pyautogui.screenshot(region=region)
            self.cache_time = current_time
        
        return self.cache
```

## Error Handling and Recovery
### Graceful Failure
```python
def safe_main():
    """Main function with error handling and recovery."""
    try:
        main()
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except pyautogui.FailSafeException:
        print("\nFail-safe triggered: mouse moved to corner.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Attempting to recover...")
        
        # Attempt recovery
        time.sleep(2)
        safe_main()  # Restart
```

### Automatic Restart
```python
def auto_restart_bot(max_attempts=5):
    """Automatically restart bot on failure."""
    attempts = 0
    
    while attempts < max_attempts:
        try:
            print(f"\nAttempt {attempts + 1}/{max_attempts}")
            main()
        except Exception as e:
            print(f"Bot crashed: {e}")
            attempts += 1
            
            if attempts < max_attempts:
                print("Restarting in 5 seconds...")
                time.sleep(5)
            else:
                print("Maximum restart attempts reached.")
                break
```

## Testing and Debugging
### Visual Debugging Mode
```python
def debug_mode(region):
    """Debug mode to visualize scan region and detection."""
    import matplotlib.pyplot as plt
    
    print("Entering debug mode...")
    print(f"Scan region: {region}")
    
    while True:
        # Capture and display scan region
        screenshot = pyautogui.screenshot(region=region)
        gray = ImageOps.grayscale(screenshot)
        
        # Convert to numpy array for analysis
        import numpy as np
        pixels = np.array(gray)
        
        # Analyze pixels
        dark_pixels = pixels < THRESHOLD
        dark_count = np.sum(dark_pixels)
        
        print(f"Dark pixels: {dark_count}/{pixels.size}")
        print(f"Detection: {'OBSTACLE' if dark_count > 0 else 'CLEAR'}")
        
        # Display image
        plt.imshow(pixels, cmap='gray')
        plt.title(f"Scan Region - {dark_count} dark pixels")
        plt.show(block=False)
        plt.pause(0.5)
        plt.close()
        
        # Check for exit
        if input("Press Enter to continue, 'q' to quit: ").lower() == 'q':
            break
```

### Performance Metrics
```python
class PerformanceMetrics:
    """Track and display bot performance metrics."""
    
    def __init__(self):
        self.start_time = time.time()
        self.jump_count = 0
        self.successful_jumps = 0
        self.failed_jumps = 0
        self.obstacles_detected = 0
    
    def record_jump(self, successful):
        """Record jump attempt."""
        self.jump_count += 1
        if successful:
            self.successful_jumps += 1
        else:
            self.failed_jumps += 1
    
    def record_obstacle(self):
        """Record obstacle detection."""
        self.obstacles_detected += 1
    
    def display_stats(self):
        """Display current performance statistics."""
        elapsed = time.time() - self.start_time
        jump_success_rate = (self.successful_jumps / self.jump_count * 100) if self.jump_count > 0 else 0
        
        print("\n=== Performance Statistics ===")
        print(f"Time running: {elapsed:.1f} seconds")
        print(f"Total jumps: {self.jump_count}")
        print(f"Successful jumps: {self.successful_jumps}")
        print(f"Failed jumps: {self.failed_jumps}")
        print(f"Jump success rate: {jump_success_rate:.1f}%")
        print(f"Obstacles detected: {self.obstacles_detected}")
        print(f"Jumps per minute: {self.jump_count / (elapsed / 60):.1f}")
```

## Customization Options
### Configuration File
```python
import json
from pathlib import Path

def load_config(config_file="bot_config.json"):
    """Load configuration from JSON file."""
    config_path = Path(config_file)
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    else:
        # Default configuration
        default_config = {
            "threshold": 120,
            "scan_width": 140,
            "scan_height": 30,
            "offset_x": 80,
            "offset_y": 10,
            "jump_cooldown": 0.15,
            "scan_delay": 0.01,
            "adaptive_threshold": True,
            "debug_mode": False
        }
        
        # Save default config
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=2)
        
        return default_config

def save_config(config, config_file="bot_config.json"):
    """Save configuration to JSON file."""
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
```

### Command Line Arguments
```python
import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Chrome Dino Game Bot")
    
    parser.add_argument("--threshold", type=int, default=120,
                       help="Detection threshold (0-255)")
    parser.add_argument("--width", type=int, default=140,
                       help="Scan region width")
    parser.add_argument("--height", type=int, default=30,
                       help="Scan region height")
    parser.add_argument("--offset-x", type=int, default=80,
                       help="Horizontal offset from dino")
    parser.add_argument("--offset-y", type=int, default=10,
                       help="Vertical offset from dino")
    parser.add_argument("--debug", action="store_true",
                       help="Enable debug mode")
    parser.add_argument("--config", type=str,
                       help="Configuration file path")
    
    return parser.parse_args()
```

## Project Purpose
This project demonstrates:
- Game automation and bot development
- Screen capture and image processing techniques
- Real-time computer vision applications
- Coordinate-based input simulation
- Performance optimization for real-time processing
- Error handling and recovery strategies
- Configuration management for adaptable software
- Testing and debugging methodologies for automation