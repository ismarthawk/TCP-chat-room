from http import client
from socket import socket
import threading

from numpy import broadcast

server = socket()
while True:
    port = int(input('Enter Port to Host the server : '))
    try:
        server.bind(('localhost', port))
        break
    except:
        print('Please try a different Port')

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} LEFT')
            del nicknames[index]
            break


while True:
    client, address = server.accept()

    client.send('NICK : '.encode())
    nickname = client.recv(1024).decode()
    nicknames.append(nickname)
    clients.append(client)

    broadcast(f'{nickname} joined the Chat')
    client.send('Connected To server'.encode())
    threading.Thread(target=handle, args=(client,)).start()
