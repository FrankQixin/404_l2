
import time,socket,sys
from multiprocessing import Process


HOST=""
ext_host='www.google.com'
PORT=8001
ext_port=80
BUFFER_SIZE=2048


#TODO:get_remote_ip
	
def get_remote_ip(host):
	print("Getting IP for {host}")
	try:
		remote_ip=socket.gethostbyname(host)
	except socket.gaierror:
		print("Host name invalid")
		sys.exit()

	print(f'IP address for {host} is {remote_ip}')
	return remote_ip


#TODO: handle_request

def handle_request(connection,address):
	print(f'connected by {address}')
	data=connection.recv(BUFFER_SIZE)
	connection.sendall(data)
	connection.shutdown(socket.SHUT_RDWR)
	connection.close()



def main():

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
		proxy_start.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		proxy_start.bind((HOST,PORT))
		proxy_start.listen(10)
		print("Starting Proxy Server on Port 8001")
		
		while True:
			
			# Receive connection from client
			connection, address = proxy_start.accept()
			print("Receiving Connection from:", address)
			remote_ip=get_remote_ip(ext_host)

			p=Process(target=handle_request,args=(connection,address))
			p.daemon=True
			p.start()
			print("Start process" ,p)
			proxy_end.shutdown(socket.SHUT_WR)


			connection.close()
				
if __name__  == "__main__":
	main()	