import socket
import pickle

# Function to process job applications
def process_application(data):
    # Process the received data (e.g., simulate evaluating the job application)
    applicant_name = data.get('name')
    experience = data.get('experience')
    skills = data.get('skills')

    # Perform some basic evaluation (example: if years of experience > 3, consider for the job)
    if experience > 3:
        return f"Congratulations {applicant_name}! Your application has been accepted."
    else:
        return f"Sorry {applicant_name}, your application does not meet the required experience."

# Create an IPv6 socket
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to localhost and a specific port
server_address = ('::1', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening...")

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = connection.recv(1024)
        if data:
            # Deserialize received data
            received_data = pickle.loads(data)
            print("Received data from client:", received_data)

            # Process the application
            response = process_application(received_data)

            # Send the response back to the client
            connection.sendall(response.encode())

    finally:
        # Clean up the connection
        connection.close()