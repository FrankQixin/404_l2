import socket,time,sys
from multiprocessing import Process

HOST=""
PORT=8001
BUFFER_SIZE=2048

def main():

	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((HOST,PORT))
		s.listen(2)

		while True:
			conn,addr=s.accept()
			p=Process(target=handle_echo,args=(addr,conn))
			p.daemon=True
			p.start()
			print("start process",p)


def handle_echo(addr,conn):
	print("connected by " ,addr)
	data=conn.recv(BUFFER_SIZE)
	conn.sendall(data)
	conn.shutdown(socket.SHUT_RDWR)
	conn.close()


        
if __name__ == "__main__":
    main()
