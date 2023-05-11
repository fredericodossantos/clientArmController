import socket

# The IP address and port of the C# TCP server
ip = '127.0.0.1'
port = 50000

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# Send a "rotate" command to the server
command = "rotate Arm_1 30 45"
client_socket.sendall(command.encode())

# Wait for a response from the server (optional)
response = client_socket.recv(1024).decode()
print("Server response:", response)

# Close the connection
client_socket.close()
