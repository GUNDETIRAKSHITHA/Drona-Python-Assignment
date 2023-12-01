

import socket

host = 'localhost' 
port = 5000

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    s.bind(('', port))

    # Listen for incoming connections
    s.listen(1)

    # Accept a connection
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))

    # Send a welcome message
    c.send(b"HELLO, How are you ? Welcome to the World")

    # Send a farewell message
    msg = "Bye.............."
    c.send(msg.encode())

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    # Close the connection and the socket in a finally block
    if 'c' in locals():
        c.close()
    if 's' in locals():
        s.close()
