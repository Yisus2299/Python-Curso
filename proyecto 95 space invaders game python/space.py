import turtle

# Base class for any game object that uses Turtle
class Actor(turtle.Turtle):
    def __init__(self, shape, color, x, y, scale=1):
        super().__init__(shape=shape)
        self.color(color)
        self.penup()               # Do not draw lines when moving
        self.speed(0)              # Instant movement
        self.shapesize(scale, scale)
        self.goto(x, y)

# Player ship class
class Player(Actor):
    def __init__(self):
        super().__init__("triangle", "cyan", 0, -240)
        self.setheading(90)        # Point the ship upward
        self.step = 20             # Movement increment per key press

    def move(self, direction):
        x = self.xcor() + direction * self.step
        x = max(-360, min(360, x))  # Keep player inside screen bounds
        self.setx(x)

# Bullet class for the player's shot
class Bullet(Actor):
    def __init__(self):
        super().__init__("triangle", "yellow", 0, -400, 0.5)
        self.active = False        # Whether the bullet is currently flying
        self.step = 25             # Bullet speed per frame
        self.hideturtle()          # Hide until fired

    def fire(self, x, y):
        if not self.active:        # Only fire one bullet at a time
            self.goto(x, y + 10)
            self.showturtle()
            self.active = True

    def update(self):
        if self.active:
            self.sety(self.ycor() + self.step)
            if self.ycor() > 280:  # Off-screen reset
                self.reset()

    def reset(self):
        self.hideturtle()
        self.active = False
        self.goto(0, -400)         # Move off-screen until next shot

# Alien enemy class
class Alien(Actor):
    def __init__(self, x, y):
        super().__init__("circle", "green", x, y)

# Barrier block class
class Barrier(Actor):
    def __init__(self, x, y):
        super().__init__("square", "white", x, y)

    def destroy(self):
        self.hideturtle()          # Remove barrier block when hit

# Main game controller class
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 700)
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders")
        self.screen.tracer(0)       # Manual screen update for smoother animation

        self.player = Player()
        self.bullet = Bullet()
        self.aliens = self.make_aliens()
        self.barriers = self.make_barriers()

        self.alien_speed = 5
        self.alien_direction = 1
        self.score = 0

        self.score_pen = self.make_score_pen()
        self.bind_keys()
        self.loop()                 # Start the game loop

    def make_score_pen(self):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.color("white")
        pen.goto(-360, 310)
        pen.write("Score: 0", font=("Arial", 16, "normal"))
        return pen

    def make_aliens(self):
        aliens = []
        for row in range(4):
            for col in range(8):
                x = -320 + col * 80
                y = 250 - row * 60
                aliens.append(Alien(x, y))
        return aliens

    def make_barriers(self):
        blocks = []
        for bx in (-240, -80, 80, 240):
            for row in range(3):
                for col in range(4):
                    blocks.append(Barrier(bx + col * 20, -140 + row * 20))
        return blocks

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(lambda: self.player.move(-1), "Left")
        self.screen.onkeypress(lambda: self.player.move(1), "Right")
        self.screen.onkeypress(
            lambda: self.bullet.fire(self.player.xcor(), self.player.ycor()),
            "space"
        )

    def loop(self):
        self.move_aliens()         # Move aliens each frame
        self.bullet.update()       # Move bullet if fired
        self.check_collisions()    # Handle bullet hits
        self.screen.update()       # Refresh screen once per frame

        if not self.check_game_over():
            self.screen.ontimer(self.loop, 150)

    def move_aliens(self):
        edge = False
        for alien in self.aliens:
            alien.setx(alien.xcor() + self.alien_direction * self.alien_speed)
            if abs(alien.xcor()) > 360:  # Alien reached screen edge
                edge = True

        if edge:
            self.alien_direction *= -1
            for alien in self.aliens:
                alien.sety(alien.ycor() - 40)  # Move aliens down

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

    def add_score(self, points):
        self.score += points
        self.score_pen.clear()
        self.score_pen.write(
            f"Score: {self.score}",
            font=("Arial", 16, "normal")
        )

    def check_game_over(self):
        if not self.aliens:
            self.show_message("YOU WIN!", "yellow")
            return True

        for alien in self.aliens:
            if alien.ycor() < -220 or alien.distance(self.player) < 20:
                self.show_message("GAME OVER", "red")
                return True

        return False

    def show_message(self, text, color):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.color(color)
        writer.penup()
        writer.goto(0, 0)
        writer.write(text, align="center", font=("Arial", 36, "bold"))

Game()
turtle.mainloop()