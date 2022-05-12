from socket import socket
socket = socket()
while True:
    port = int(input('Enter the port Number : '))
    try:
        socket.bind(('', port))
        break
    except:
        print('Port is already in use, try another port')
print('Server is running on port : ', port)
socket.listen()

while True:
    conn, addr = socket.accept()
