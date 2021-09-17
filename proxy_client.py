import socket, time

HOST ="localhost"
PORT = 8001
BUFFER_SIZE = 2048

payload='GET / HTTP/1.0\r\nHost:  www.google.com\r\n\r\n'

def conenct(addr):
    try :
        s=socket.socket(socket.AF_INET.socket.SOCK_STREAM)
        s.conenct(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        data=s.recv(BUFFER_SIZE)
        print(data)
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    conenct((HOST,PORT))



        
if __name__ == '__main__':
    main()
