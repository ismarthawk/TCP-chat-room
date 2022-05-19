from multiprocessing.connection import Client
import threading
from socket import socket

nickname = input("Enter the NickName")
client = socket()
port = int(input('Enter port to connect'))
client.connect(('localhost', port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(f'{nickname}'.encode())
            else:
                print(message)
        except:
            print('Error Occoured')
            client.close()
            break


def write():
    while True:
        message = '{} : {}'.format(nickname, input(''))
        client.send(message.encode())
