import socket

import socket
import pickle

# Create an IPv6 socket
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Connect to the server at localhost and the specified port
server_address = ('::1', 8080)
client_socket.connect(server_address)

try:
    # Get job application information from the user
    name = input("Enter your name: ")
    experience = int(input("Enter years of experience: "))
    skills = input("Enter your skills (comma-separated): ").split(',')

    # Prepare job application data
    job_application = {
        'name': name,
        'experience': experience,
        'skills': skills
    }

    # Send job application data to the server
    serialized_data = pickle.dumps(job_application)
    client_socket.sendall(serialized_data)

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Server's response: {response.decode()}")

finally:
    # Clean up the connection
    client_socket.close()
