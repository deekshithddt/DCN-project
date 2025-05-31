import socket
from email.parser import Parser

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server_socket.bind(('localhost', 12345))  # Bind to localhost and port 12345
    server_socket.listen(5)  # Listen for up to 5 connections

    print("Server is listening on port 12345...")

    while True:
        conn, addr = server_socket.accept()  # Accept incoming connection
        print(f"\nConnected by {addr}")

        while True:
            # Receive email data
            email_data = conn.recv(4096).decode('utf-8')  # Receive up to 4096 bytes
            if not email_data:
                break  # Break if the client disconnects
            
            print("Raw MIME Email received:\n", email_data)

            # Parse the email data
            email_message = Parser().parsestr(email_data)
            print("\nParsed Email Details:")
            print(f"From: {email_message['From']}")
            print(f"To: {email_message['To']}")
            print(f"Subject: {email_message['Subject']}")
            print("\nBody:")
            print(email_message.get_payload())

            # Enter a custom acknowledgment message
            ack_message = input("\nEnter acknowledgment for this email: ")
            conn.send(ack_message.encode('utf-8'))

        conn.close()  # Close the connection
        print(f"Connection with {addr} closed.")

tcp_server()
