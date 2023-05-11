import socket

# Set the server address and port
server_address = ('localhost', 50000)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
client_socket.connect(server_address)

# Define the message to send to the server
message = 'Arm_2 rotate y 45 10'

# Send the message to the server
client_socket.sendall(message.encode())

# Close the socket
client_socket.close()
