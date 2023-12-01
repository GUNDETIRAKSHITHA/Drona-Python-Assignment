import turtle

# Define screen dimensions and background color
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

# Create a turtle object for the drone
drone = turtle.Turtle()
drone.speed(0)
drone.penup()

# Define color and size of drone body
body_color = "blue"
body_radius = 15

# Draw the drone body as a circle
drone.fillcolor(body_color)
drone.begin_fill()
drone.circle(body_radius)
drone.end_fill()

# Draw the propeller as a smaller circle on top
propeller_color = "yellow"
propeller_radius = 5
drone.penup()
drone.goto(0, body_radius + propeller_radius)
drone.pendown()
drone.fillcolor(propeller_color)
drone.begin_fill()
drone.circle(propeller_radius)
drone.end_fill()

# Define functions to move the drone
def move_forward(distance):
    drone.forward(distance)

def move_backward(distance):
    drone.backward(distance)

def move_left(angle):
    drone.left(angle)

def move_right(angle):
    drone.right(angle)

# Bind keyboard keys to movement functions
screen.onkey(lambda: move_forward(5), "Up")
screen.onkey(lambda: move_backward(5), "Down")
screen.onkey(lambda: move_left(5), "Left")
screen.onkey(lambda: move_right(5), "Right")

# Start listening for keyboard events
screen.listen()

# Example usage of movement functions
move_forward(50)
move_right(90)
move_backward(30)
move_left(45)

# Keep the window open
turtle.done()
