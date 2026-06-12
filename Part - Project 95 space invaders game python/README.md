# Space Invaders Game

A classic Space Invaders arcade game built with Python and the turtle graphics library.

## Overview

This project is a complete Space Invaders clone featuring a player-controlled spaceship, alien enemies, projectiles, barriers, score tracking, and win/lose conditions. The game demonstrates object-oriented programming principles with Python's turtle graphics module.

## Features

- **Player Ship**: Move left/right to avoid aliens
- **Shooting**: Fire projectiles to destroy aliens
- **Alien Enemies**: Grid of 32 aliens (4 rows × 8 columns)
- **Barriers**: 4 defensive barriers that can be destroyed
- **Score System**: Points for destroying aliens (+10 per alien)
- **Win/Lose Conditions**: Win by clearing all aliens, lose if aliens reach the player
- **Smooth Animation**: 150ms game loop for fluid gameplay

## Tech Stack

- **Language**: Python
- **Graphics**: turtle (Python standard library)
- **No external dependencies**: Uses only standard library

## Project Structure

```
Part - Project 95 space invaders game python/
├── space.py    # Main game file
└── README.md   # This file
```

## Installation & Running

No additional dependencies required:

```bash
python space.py
```

## Controls

| Key | Action |
|-----|--------|
| Left Arrow | Move ship left |
| Right Arrow | Move ship right |
| Spacebar | Fire bullet |

## Game Components

### Actor Class (Base)
```python
class Actor(turtle.Turtle):
    def __init__(self, shape, color, x, y, scale=1):
        # Initialize turtle with shape, color, position
        super().__init__(shape=shape)
        self.color(color)
        self.penup()
        self.speed(0)
        self.shapesize(scale, scale)
        self.goto(x, y)
```

Base class for all game objects.

### Player Class
```python
class Player(Actor):
    def __init__(self):
        super().__init__("triangle", "cyan", 0, -240)
        self.setheading(90)
        self.step = 20
    
    def move(self, direction):
        x = self.xcor() + direction * self.step
        x = max(-360, min(360, x))  # Screen bounds
        self.setx(x)
```

- Shape: Triangle (pointing up)
- Color: Cyan
- Movement: 20 pixels per key press
- Bounds: -360 to 360 (stays on screen)

### Bullet Class
```python
class Bullet(Actor):
    def __init__(self):
        super().__init__("triangle", "yellow", 0, -400, 0.5)
        self.active = False
        self.step = 25
        self.hideturtle()
    
    def fire(self, x, y):
        if not self.active:
            self.goto(x, y + 10)
            self.showturtle()
            self.active = True
    
    def update(self):
        if self.active:
            self.sety(self.ycor() + self.step)
            if self.ycor() > 280:
                self.reset()
    
    def reset(self):
        self.hideturtle()
        self.active = False
        self.goto(0, -400)
```

- Only one bullet at a time
- Speed: 25 pixels per frame
- Resets when leaving screen

### Alien Class
```python
class Alien(Actor):
    def __init__(self, x, y):
        super().__init__("circle", "green", x, y)
```

- Shape: Circle
- Color: Green
- 32 aliens in formation (4 rows × 8 columns)

### Barrier Class
```python
class Barrier(Actor):
    def __init__(self, x, y):
        super().__init__("square", "white", x, y)
    
    def destroy(self):
        self.hideturtle()
```

- Shape: Square
- Color: White
- 48 total barriers (4 groups × 3 rows × 4 columns)
- Destroyed when hit by bullet

## Game Class (Main Controller)

```python
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 700)
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")
        self.screen.tracer(0)
        
        # Initialize objects
        self.player = Player()
        self.bullet = Bullet()
        self.aliens = self.make_aliens()
        self.barriers = self.make_barriers()
        
        # Game state
        self.alien_speed = 5
        self.alien_direction = 1
        self.score = 0
        
        # Start game loop
        self.bind_keys()
        self.loop()
```

### Screen Setup
- Size: 800 × 700 pixels
- Background: Black
- Tracer: 0 (manual updates for smoother animation)

### Alien Formation

```python
def make_aliens(self):
    aliens = []
    for row in range(4):
        for col in range(8):
            x = -320 + col * 80
            y = 250 - row * 60
            aliens.append(Alien(x, y))
    return aliens
```

| Row | Y Position |
|-----|------------|
| 0 | 250 |
| 1 | 190 |
| 2 | 130 |
| 3 | 70 |

Columns: -320 to 320 (8 aliens, 80px spacing)

### Barrier Formation

```python
def make_barriers(self):
    blocks = []
    for bx in (-240, -80, 80, 240):      # 4 barrier groups
        for row in range(3):              # 3 rows per group
            for col in range(4):          # 4 blocks per row
                blocks.append(Barrier(bx + col * 20, -140 + row * 20))
    return blocks
```

48 total barrier blocks protecting the player.

### Key Bindings

```python
def bind_keys(self):
    self.screen.listen()
    self.screen.onkeypress(lambda: self.player.move(-1), "Left")
    self.screen.onkeypress(lambda: self.player.move(1), "Right")
    self.screen.onkeypress(
        lambda: self.bullet.fire(self.player.xcor(), self.player.ycor()),
        "space"
    )
```

## Game Loop

```python
def loop(self):
    self.move_aliens()
    self.bullet.update()
    self.check_collisions()
    self.screen.update()
    
    if not self.check_game_over():
        self.screen.ontimer(self.loop, 150)  # ~7 FPS
```

Runs every 150ms (~7 frames per second).

### Alien Movement

```python
def move_aliens(self):
    edge = False
    for alien in self.aliens:
        alien.setx(alien.xcor() + self.alien_direction * self.alien_speed)
        if abs(alien.xcor()) > 360:
            edge = True
    
    if edge:
        self.alien_direction *= -1
        for alien in self.aliens:
            alien.sety(alien.ycor() - 40)
```

Aliens move horizontally until hitting screen edge, then move down and reverse direction.

### Collision Detection

```python
def check_collisions(self):
    if not self.bullet.active:
        return
    
    # Check bullet hits aliens
    for alien in self.aliens[:]:
        if self.bullet.distance(alien) < 20:
            alien.hideturtle()
            self.aliens.remove(alien)
            self.bullet.reset()
            self.add_score(10)
            break
    
    # Check bullet hits barriers
    for barrier in self.barriers[:]:
        if self.bullet.active and self.bullet.distance(barrier) < 15:
            barrier.destroy()
            self.barriers.remove(barrier)
            self.bullet.reset()
            break
```

- Bullet-Alien collision: Distance < 20 pixels
- Bullet-Barrier collision: Distance < 15 pixels

### Win/Lose Conditions

```python
def check_game_over(self):
    # Win: All aliens destroyed
    if not self.aliens:
        self.show_message("YOU WIN!", "yellow")
        return True
    
    # Lose: Aliens reach player or touch player
    for alien in self.aliens:
        if alien.ycor() < -220 or alien.distance(self.player) < 20:
            self.show_message("GAME OVER", "red")
            return True
    
    return False
```

## Scoring System

```python
def add_score(self, points):
    self.score += points
    self.score_pen.clear()
    self.score_pen.write(
        f"Score: {self.score}",
        font=("Arial", 16, "normal")
    )
```

- +10 points per alien destroyed
- Score displayed at top-left of screen

## Game Flow

1. **Start**: Game initializes with aliens and barriers
2. **Play**: Move ship, shoot aliens, avoid being touched
3. **Win**: All aliens destroyed → "YOU WIN!" message
4. **Lose**: Alien reaches bottom or touches player → "GAME OVER"

## Customization

### Increase Difficulty

```python
self.alien_speed = 10  # Faster aliens (default: 5)
```

### Change Bullet Speed

```python
self.step = 40  # Faster bullet (default: 25)
```

### More Points Per Alien

```python
self.add_score(20)  # +20 points (default: 10)
```

### More Aliens

```python
# Add more rows
for row in range(6):  # 6 rows instead of 4
```

### Change Colors

```python
# In each class
self.color("red")  # Change alien color
self.color("orange")  # Change barrier color
```

## Code Architecture Summary

```
Actor (base class)
├── Player (user-controlled ship)
├── Bullet (projectile)
├── Alien (enemy)
└── Barrier (defense)

Game (main controller)
├── Setup screen
├── Create game objects
├── Handle input
├── Game loop
├── Collision detection
└── Win/lose logic
```

## Troubleshooting

### Game doesn't respond to keys
- Click on the game window first to give it focus

### Game too fast/slow
- Adjust the timer in `self.screen.ontimer(self.loop, 150)`
- Lower value = faster game

### Screen too small/large
- Modify `self.screen.setup(800, 700)`

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)