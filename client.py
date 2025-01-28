import socket

SERVER_IP = "192.168.1.24"  # Replace with server's IP
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, PORT))
        print("Connected to the server.")
        while True:
            message = input("Enter message (or 'exit' to quit): ")
            if message.lower() == "exit":
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Server reply: {data.decode()}")

if __name__ == "__main__":
    main()
