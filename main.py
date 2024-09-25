import socket
import threading

# Configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6809          # The port used by the EuroScope server

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode('utf-8').strip()
            print(f"Received: {message}")
            
            # Respond back to EuroScope
            #response = "ACK: " + message  # Example response
            #conn.sendall(response.encode('utf-8'))
    finally:
        conn.close()
        print(f"Connection closed by {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
