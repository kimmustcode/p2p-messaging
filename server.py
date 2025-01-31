import socket
import threading

HOST = "0.0.0.0"  # listens on all network interfaces
PORT = 65432      
connections = []

def clientConnection(client_socket, client_address):
    bumper = "\n-----------------------\n"
    with client_socket:
        print(f"{bumper}New connection from {client_address[0]}{bumper}")
        connections.append(client_socket)
        while True:
            try: 
                data = client_socket.recv(1024)
                if not data:
                    print(f"{bumper}{client_address[0]} has disconnected...{bumper}")
                    print(f"Current connections: {threading.active_count() - 1}")
                    break     
                
                msg = f"{client_address[0]}: {data.decode()}"
                print(msg)
                for user in connections:
                    user.sendall(msg.encode())

            except:
                print(f"{bumper}Connection lost with {client_address[0]}{bumper}")
                connections.remove(client_socket)
                print(f"Current connections: {threading.active_count() - 1}")

def main(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))

        while True:
            server_socket.listen()
            client_socket, client_address = server_socket.accept()

            thread = threading.Thread(target=clientConnection, args=(client_socket, client_address), daemon=True)
            thread.start()
            print(f"Current connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
