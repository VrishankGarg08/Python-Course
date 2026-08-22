import turtle

# Create the turtle
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(3)

# Draw the square
for i in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open
turtle.done()