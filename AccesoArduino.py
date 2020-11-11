import socket
HOST = '192.168.4.1'
PORT = 80

def enviarOrdenArduino(input):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(input)
        s.close()
