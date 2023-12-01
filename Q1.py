import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Drone Movement Simulator")

# Create a drone turtle
drone = turtle.Turtle()
drone.shape("triangle")
drone.color("blue")
drone.speed(2)

# Function to move the drone forward
def move_forward():
    drone.forward(50)

# Function to move the drone backward
def move_backward():
    drone.backward(50)

# Function to move the drone left
def move_left():
    drone.left(90)

# Function to move the drone right
def move_right():
    drone.right(90)

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# Close the window on click
screen.exitonclick()
