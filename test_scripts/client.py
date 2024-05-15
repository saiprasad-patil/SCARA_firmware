import socket

# Server configuration
SERVER_HOST = '192.168.0.105'  # Replace with the actual IP address of PC 1
SERVER_PORT = 12345        # Same port used by the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

print('Connected to the server.')

try:
    while True:
        # Input value to send
        value = '2'

        if value.lower() == 'quit':
            break

        # Send value to the server
        client_socket.sendall(value.encode())
        print("Value sent.")

except KeyboardInterrupt:
    print('Client terminated by user.')

finally:
    # Close the socket
    client_socket.close()
