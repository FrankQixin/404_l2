import sys,socket

def create_tcp_socket():
	print("create_tcp_socket")
	try :
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except(socket.error,msg):
		print("Create socket failed")
		sys.exit()
	print("socket created successfully")
	return s

def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        ssocket.sendall(payload.encode())
    except socket.error:
        print('Failed to send payload')
        sys.exit()
    print("Sent payload success")

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
	try:
            host='www.google.com'
	    port=80
	    payload= f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
	    buffer = 4096
	    google_socket=create_tcp_socket()
	    remote_ip=get_remote_ip(host)
	    google_socket.connect((remote_ip,port))
	    print (f'Socket connected to {host} on {port}')

	    send_data(google_socket,payload)
	    google_socket.shutdown(socket.SHUT_WR)
	    final_data = b""

        while True:
            data = google_socket.recv(buffer)
            if not data:
                break
            final_data += data
        print(final_data)

    except Exception as e:
        print(e)
    finally:
        google_socket.close()

if __name__ == '__main__':
    main()











