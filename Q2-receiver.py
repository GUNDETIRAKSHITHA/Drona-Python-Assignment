
import socket

host = 'localhost'  
port = 5000

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect(('127.0.0.1', port))

    # Receive and print messages
    msg = s.recv(1024)
    while msg:
        print('Received: ' + msg.decode())
        msg = s.recv(1024)

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    # Close the socket in a finally block to ensure it always gets closed
    if s:
        s.close()
