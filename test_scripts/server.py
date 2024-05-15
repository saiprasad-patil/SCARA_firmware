import socket

# Server configuration
HOST = '0.0.0.0'  # Use 0.0.0.0 to accept connections from any IP address
PORT = 12345      # Choose a free port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening for connections...')

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print(f'Connected to {client_address}')

try:
    while True:
        # Receive data from the client
        received_data = client_socket.recv(1024)

        if not received_data:
            break

        print(f'Received: {received_data.decode()}')

except KeyboardInterrupt:
    print('Server terminated by user.')

finally:
    # Close the socket
    server_socket.close()
