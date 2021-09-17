import socket, time, sys
from multiprocessing import Process

HOST = ''
end_host = 'www.google.com'
PORT = 8001
end_port = 80
BUFFER_SIZE = 2048

def handle_request(conn, addr, proxy_end):
    data = conn.recv(BUFFER_SIZE)

    proxy_end.sendall(data)

    proxy_end.shutdown(socket.SHUT_WR)
    
    end_data = b""

    while True:
        data = proxy_end.recv(BUFFER_SIZE)
        if not data:
            break
        end_data += data
    
    print(f"Receiving Data from {end_host}")

    time.sleep(0.5)
    conn.sendall(end_data)
    
    print("Sent Data Back to", addr)


def main():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((HOST,PORT))
        print("Starting tcp server on port 8001")

        server_socket.listen(2)

        while True:

            connection, address = server_socket.accept()
            print("Receiving connection from:", address)
            

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print(f"Connecting to {end_host}")

                proxy_end.connect((end_host, end_port))
                print(f"Connected to {end_host} and Sending Data")

                # Start a process for each incoming connection with the correct arguments
                p = Process(target=handle_request, args=(connection, address, proxy_end))
                p.daemon = True
                p.start()
                print("Start new process", p)
                

            connection.close()

if __name__ == '__main__':
    main()
