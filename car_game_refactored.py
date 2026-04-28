import turtle

# ==================================================
# 1. Screen setup
# ==================================================
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("gray")
screen.title("Car Game - Use Arrow Keys & P for Parking")
screen.tracer(0)          # smoother animation (manual update)

# ==================================================
# 2. Helper functions to create turtles
# ==================================================
def create_square_turtle(color, shape_size=0.2, pen_down=False):
    """Return a square-shaped turtle with basic settings."""
    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(shape_size)
    t.color(color)
    t.penup()
    if pen_down:
        t.pendown()
    return t

def create_circle_turtle(color, radius=1):
    """Return a circle-shaped turtle."""
    t = turtle.Turtle()
    t.shape("circle")
    t.shapesize(radius)
    t.color(color)
    t.penup()
    return t

def draw_horizontal_line(y, width=1000, color="white"):
    """Draw a horizontal line from x=-400 to x=-400+width."""
    line = create_square_turtle(color, shape_size=0.2, pen_down=True)
    line.goto(-400, y)
    line.forward(width)
    line.penup()
    return line

# ==================================================
# 3. Road lines (top and bottom)
# ==================================================
top_road_line = draw_horizontal_line(200)
bottom_road_line = draw_horizontal_line(-200)

# ==================================================
# 4. Decorative road blocks (white/yellow squares)
# ==================================================
decorative_turtles = []

x_positions = [-350, -300, -250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350]
colors_cycle = ["white", "yellow"]

for i, x in enumerate(x_positions):
    color = colors_cycle[i % 2]

    t_up = create_square_turtle(color, shape_size=5)
    t_up.goto(x, 250)
    decorative_turtles.append(t_up)

    t_down = create_square_turtle(color, shape_size=5)
    t_down.goto(x, -250)
    decorative_turtles.append(t_down)

# ==================================================
# 5. Build the car (4 parts: body front/back + headlights)
# ==================================================
car_parts = []

# Rear and front body (red squares)
car_body_rear = create_square_turtle("red", shape_size=4)
car_body_rear.goto(-340, 130)
car_parts.append(car_body_rear)

car_body_front = create_square_turtle("red", shape_size=4)
car_body_front.goto(-315, 130)
car_parts.append(car_body_front)

# Blue headlights
headlight_left = create_circle_turtle("blue", radius=1)
headlight_left.goto(-350, 90)
car_parts.append(headlight_left)

headlight_right = create_circle_turtle("blue", radius=1)
headlight_right.goto(-300, 90)
car_parts.append(headlight_right)

# ==================================================
# 6. Core movement function
# ==================================================
def move_car(angle, steps=3):
    """Move all car parts in the given angle by 'steps' pixels."""
    for part in car_parts:
        part.setheading(angle)
        part.forward(steps)
    update_screen()

def update_screen():
    """Refresh the screen for smooth movement."""
    screen.update()

# ==================================================
# 7. Keyboard action functions
# ==================================================
def move_right():
    move_car(0)      # 0° = right

def move_left():
    move_car(180)    # 180° = left

def move_up():
    move_car(90)     # 90° = up

def move_down():
    move_car(-90)    # -90° = down

def park_car():
    """Teleport the car back to its starting position."""
    car_body_rear.goto(-340, 130)
    car_body_front.goto(-315, 130)
    headlight_left.goto(-350, 90)
    headlight_right.goto(-300, 90)
    update_screen()

# ==================================================
# 8. Bind keys
# ==================================================
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(park_car, "p")
screen.listen()

# ==================================================
# 9. Main game loop
# ==================================================
while True:
    update_screen()
