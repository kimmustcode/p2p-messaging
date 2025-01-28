import socket
HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 65432      # Port to bind to


def clientConnection(client_socket, client_address):
        with client_socket:
            print(f"Connected by {client_address}")
            while True:
                try: 
                    data = client_socket.recv(1024)
                    if not data:
                        print(f"{client_address} has disconnected...")
                        break     
                        
                    print(f"{client_address[0]}: {data.decode()}")
                    client_socket.sendall(b"Message received!")

                except:
                    print(f"Connection lost with {client_address[0]}")

def main(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server listening on {HOST}:{PORT}...")

        client_socket, client_address = server_socket.accept()

        clientConnection(client_socket, client_address)



if __name__ == "__main__":
    main()
