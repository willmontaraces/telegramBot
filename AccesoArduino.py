import socket
HOST = '192.168.4.1'
PORT = 80

def enviarOrdenArduino(input):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        input = input + '\r\n'
        s.sendall(bytes(input, 'ascii'))
        s.close()
