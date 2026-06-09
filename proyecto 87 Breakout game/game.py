import turtle
import time
import random

# ----------------------------
# CONFIGURACION GENERAL
# ----------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_STEP = 35

BALL_SPEED_X = 3.0
BALL_SPEED_Y = 3.0

BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = 70
BRICK_HEIGHT = 20
BRICK_PADDING = 6
TOP_MARGIN = 70

LIVES_START = 3

# ----------------------------
# PANTALLA
# ----------------------------
screen = turtle.Screen()
screen.title("Breakout Clone - Python Turtle")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# ----------------------------
# PADDLE
# ----------------------------
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_WIDTH / 20)  # ancho aprox
paddle.penup()
paddle.goto(0, -250)

def move_left():
    x = paddle.xcor() - PADDLE_STEP
    min_x = -SCREEN_WIDTH // 2 + PADDLE_WIDTH // 2
    if x < min_x:
        x = min_x
    paddle.setx(x)

def move_right():
    x = paddle.xcor() + PADDLE_STEP
    max_x = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
    if x > max_x:
        x = max_x
    paddle.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# ----------------------------
# PELOTA
# ----------------------------
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, -120)
ball.dx = BALL_SPEED_X * random.choice([-1, 1])
ball.dy = BALL_SPEED_Y

def reset_ball():
    ball.goto(0, -120)
    ball.dx = BALL_SPEED_X * random.choice([-1, 1])
    ball.dy = BALL_SPEED_Y

# ----------------------------
# SCORE / VIDAS
# ----------------------------
score = 0
lives = LIVES_START

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 260)

def update_hud():
    pen.clear()
    pen.write(f"Score: {score}    Lives: {lives}", align="center", font=("Arial", 16, "bold"))

update_hud()

# ----------------------------
# BLOQUES
# ----------------------------
brick_colors = ["#ff4d4d", "#ff944d", "#ffd24d", "#8cff66", "#66ccff"]
bricks = []

start_x = -(BRICK_COLS * (BRICK_WIDTH + BRICK_PADDING) - BRICK_PADDING) / 2 + BRICK_WIDTH / 2
start_y = SCREEN_HEIGHT // 2 - TOP_MARGIN

for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_colors[row % len(brick_colors)])
        brick.shapesize(stretch_wid=BRICK_HEIGHT / 20, stretch_len=BRICK_WIDTH / 20)
        brick.penup()
        x = start_x + col * (BRICK_WIDTH + BRICK_PADDING)
        y = start_y - row * (BRICK_HEIGHT + BRICK_PADDING)
        brick.goto(x, y)
        bricks.append(brick)

# ----------------------------
# UTILIDADES COLISION
# ----------------------------
def ball_hits_paddle():
    # Comprobacion AABB simple
    bx, by = ball.xcor(), ball.ycor()
    px, py = paddle.xcor(), paddle.ycor()
    half_pw = PADDLE_WIDTH / 2
    half_ph = 10  # alto aproximado de la paleta
    radius = 10   # radio aproximado de la pelota

    overlap_x = abs(bx - px) <= (half_pw + radius)
    overlap_y = abs(by - py) <= (half_ph + radius)
    return overlap_x and overlap_y and ball.dy < 0

def ball_hits_brick(brick):
    bx, by = ball.xcor(), ball.ycor()
    rx, ry = brick.xcor(), brick.ycor()
    half_rw = BRICK_WIDTH / 2
    half_rh = BRICK_HEIGHT / 2
    radius = 10

    overlap_x = abs(bx - rx) <= (half_rw + radius)
    overlap_y = abs(by - ry) <= (half_rh + radius)
    return overlap_x and overlap_y

def game_over(message):
    text = turtle.Turtle()
    text.hideturtle()
    text.color("white")
    text.penup()
    text.goto(0, 0)
    text.write(message, align="center", font=("Arial", 24, "bold"))

# ----------------------------
# BUCLE PRINCIPAL
# ----------------------------
running = True

while running:
    screen.update()
    time.sleep(0.01)

    # Mover pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Rebote en paredes laterales
    if ball.xcor() > SCREEN_WIDTH // 2 - 10:
        ball.setx(SCREEN_WIDTH // 2 - 10)
        ball.dx *= -1
    elif ball.xcor() < -SCREEN_WIDTH // 2 + 10:
        ball.setx(-SCREEN_WIDTH // 2 + 10)
        ball.dx *= -1

    # Rebote techo
    if ball.ycor() > SCREEN_HEIGHT // 2 - 10:
        ball.sety(SCREEN_HEIGHT // 2 - 10)
        ball.dy *= -1

    # Colision con paleta
    if ball_hits_paddle():
        # Rebota hacia arriba
        ball.sety(paddle.ycor() + 15)
        ball.dy = abs(ball.dy)

        # Efecto "angulo": segun donde pegue en la paleta
        offset = (ball.xcor() - paddle.xcor()) / (PADDLE_WIDTH / 2)
        ball.dx += offset * 1.2
        ball.dx = max(min(ball.dx, 7), -7)

    # Colision con bloques
    hit_brick = None
    for brick in bricks:
        if ball_hits_brick(brick):
            hit_brick = brick
            break

    if hit_brick:
        hit_brick.hideturtle()
        bricks.remove(hit_brick)
        score += 10
        update_hud()

        # Rebote simple al romper bloque
        ball.dy *= -1

    # Si cae abajo
    if ball.ycor() < -SCREEN_HEIGHT // 2:
        lives -= 1
        update_hud()

        if lives <= 0:
            game_over("GAME OVER")
            running = False
        else:
            reset_ball()

    # Si no quedan bloques, gana
    if len(bricks) == 0:
        game_over("YOU WIN!")
        running = False

screen.mainloop()