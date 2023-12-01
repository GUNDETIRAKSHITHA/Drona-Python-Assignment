# Drona-Python-Assignment
## Q1-Simulated Drone Movement System

This Python program uses the Turtle module to simulate the movement of a drone. The drone can move in four directions: forward, backward, left, and right.

## Setup
1. Make sure you have Python installed on your machine.
2. Install the Turtle module by running the following command:
   ```bash
   pip install PythonTurtle
## Usage
Clone the repository or download the Python script (Q1.py).
Open a terminal or command prompt in the directory where the script is located.
Run the script using the following command:
python Q1.py
The Turtle graphics window will appear, displaying a blue drone with a yellow propeller.
Control the drone using the arrow keys on your keyboard:
Up Arrow: Move the drone forward
Down Arrow: Move the drone backward
Left Arrow: Turn the drone to the left
Right Arrow: Turn the drone to the right
Example
The program includes example usage of movement functions, moving the drone forward, turning right, moving backward, and turning left.

Notes
Close the Turtle graphics window to exit the program.
Feel free to modify the code to customize the appearance or behavior of the drone.
# Output
![Q1_output img](https://github.com/GUNDETIRAKSHITHA/Drona-Python-Assignment/assets/97968070/e88c9a3f-78a7-4603-be24-a98dad607229)
https://github.com/GUNDETIRAKSHITHA/Drona-Python-Assignment/assets/97968070/c47f026e-4f23-4509-8e56-1ef599463193

## Q2-TCP Socket Communication

# Usage

Server (receiver): Run the receiver.py script on the server.
python receiver.py

The server will bind to the specified port and wait for incoming connections.

Client (sender): Run the sender.py script on the client.
python sender.py
The client will connect to the server and send a welcome message, followed by a farewell message.

# Error Handling
The code includes error handling for socket operations to ensure a graceful exit in case of any issues.

If a socket error occurs, an exception message will be printed, and the program will attempt to close the socket and the connection.

# Notes
Make sure to run the server script before the client to establish a connection.
The scripts use the loopback address (localhost), and the default port is set to 5000. You can modify the host and port variables in the code if needed.

## Output

![Q2_output img](https://github.com/GUNDETIRAKSHITHA/Drona-Python-Assignment/assets/97968070/85b812be-2984-48b8-b39e-0f83f19b7c55)
