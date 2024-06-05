import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=650)
screen.bgcolor("sky blue")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to the fastest

# Define Christmas tree color
tree_color = "forest green"

# List of colors for the decoration balls
balls_color = ["red", "blue", "yellow", "purple", "pink", "orange"]

decorations = []

# Function to draw a triangle (part of the tree)
def draw_triangle(color, position, size):
    t.penup()
    t.goto(position)
    t.pendown()
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(size / 2)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size / 2)
    t.end_fill()

# Function to draw a decoration ball
def draw_ball(color, x, y):
    ball = turtle.Turtle()
    ball.speed(0)
    ball.penup()
    ball.goto(x, y)
    ball.color(color)
    ball.shape("circle")
    ball.shapesize(0.5)  # Set ball size
    decorations.append(ball)  # Add ball to the list

# Function to draw a star
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Function to draw the Christmas tree
def draw_christmas_tree():
    # Draw the tree sections
    positions = [(0, -100), (0, -60), (0, -20), (0, 20)]
    sizes = [240, 200, 160, 120]

    for position, size in zip(positions, sizes):
        draw_triangle(tree_color, position, size)
    
    # Draw the decoration balls
    for _ in range(25):
        x = random.randint(-70, 70)
        y = random.randint(-100, 80)
        draw_ball(random.choice(balls_color), x, y)

    # Draw stars
    for _ in range(5):
        x = random.randint(-70, 70)
        y = random.randint(-100, 80)
        draw_star(x, y, 15)

    # Draw the tree trunk
    t.penup()
    t.goto(-15, -100)
    t.pendown()
    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.end_fill()

# Function to make the decorations glitter
def glitter():
    for ball in decorations:
        ball.color(random.choice(balls_color))
    screen.ontimer(glitter, 500)

# Draw the Christmas tree
draw_christmas_tree()

# Add glitter effect
glitter()

# Hide the turtle cursor
t.hideturtle()

# Finish drawing
turtle.done()
