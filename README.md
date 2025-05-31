# DCN-project
# 🌐 Server-Client Interaction – DCN Project

This project is a demonstration of basic client-server communication using socket programming. It was developed as part of the **Data Communication and Networking (DCN)** course to explore the core principles of computer networking and how devices communicate over a network.

## 📌 Project Objective

The goal of this project is to simulate a basic server and client interaction where:
- A server listens on a specified port and accepts incoming client connections.
- A client connects to the server and sends a message.
- The server processes the message and responds accordingly.
- The communication is maintained using **TCP/IP protocol**.

## 📁 Project Structure

server-client-dcn/
├── server.py # Python file containing server-side code
├── client.py # Python file containing client-side code
├── README.md # Project documentation
└── requirements.txt # (Optional) List of dependencies if needed

## 🛠️ Technologies Used

- **Programming Language**: Python 3
- **Networking Protocol**: TCP (Transmission Control Protocol)
- **Modules Used**: `socket`, `threading` (for multi-client support, optional)

## 🧪 How It Works

### Server:
1. Binds to a local IP address and a port.
2. Listens for incoming connections from clients.
3. Accepts a connection and waits for a message.
4. Sends a response back to the client.
5. Optionally handles multiple clients using threads.

### Client:
1. Connects to the server's IP address and port.
2. Sends a message to the server.
3. Receives and displays the server's response.

## 🚀 How to Run

### Prerequisites
- Python 3 installed on your system.

### Step 1: Start the Server
Open a terminal and run:
```bash
python server.py
python client.py
