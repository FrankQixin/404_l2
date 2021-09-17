import socket, time

HOST = ''
PORT = 8001
BUFFER_SIZE = 2048


def get_remote_ip(host):
    print("Getting IP for {host}")
    try:
        remote_ip=socket.gethostbyname(host)
    except socket.gaierror:
        print("Host name invalid")
        sys.exit()

    print(f'IP address for {host} is {remote_ip}')
    return remote_ip


def main():

    ext_host='www.google.com'
    port=80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        
        proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        proxy_start.bind((HOST,PORT))
        proxy_start.listen(1)
        print("Starting Proxy Server on Port 8081")
        
        while True:
            
            # Receive connection from client
            connection, address = proxy_start.accept()
            print("Receiving Connection from:", address)
            

            # Set up TCP socket for sending request to Google, and sends the request
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print(f"Connecting to GOOGLE")

                remote_ip=get_remote_ip(ext_host)

                proxy_end.conenct((remote_ip,port))

                send_data=connection.recv(BUFFER_SIZE)
                print(f'Sending {send_data} to GOOGLE')
                proxy_end.sendall(send_data)

                proxy_end.sendall(send_data)
                proxy_end.shutdown(socket.SHUT_WR)

                data=proxy_end.recv(BUFFER_SIZE)
                print(f'Sending recieved data {data} ')
                connection.send(data)
            connection.close()
                

        
if __name__ == '__main__':
    main()
