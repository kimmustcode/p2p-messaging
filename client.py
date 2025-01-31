import socket
import threading

SERVER_IP = "192.168.1.24"  
PORT = 65432

# Threading needed to handles listening for messages and typing messages

def messageListening():

    return 

def messageHandling(client_socket):
    while True:
            message = input("Enter message (or 'exit' to quit): ")
            if message.lower() == "exit":
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)

            if data: 
                print(data.decode())
    return


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, PORT))
        print("Connected to the server.")
        
        messageHandling(client_socket)

if __name__ == "__main__":
    main()
