import socket, time

HOST = ''
PORT = 8081
BUFFER_SIZE = 4096

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #Q3
        server_socket.bind((HOST,PORT))
        print("Starting TCP localhost Server on Port 8081")

        server_socket.listen(2)

        while True:

            # Accept incoming connection and send data back to client
            conn, addr = server_socket.accept()
            print("Connected by:", addr)
            data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            print("Sending Data:", data, "to", addr)
            conn.sendall(data)

            conn.close()


if __name__ == '__main__':
    main()








