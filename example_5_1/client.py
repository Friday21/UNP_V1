#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Page 100, 图5-4 TCP回射服务器——client
"""
import socket

# HOST = '10.242.146.194'
HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    str_cli(client_socket)


def str_cli(client_socket):
    while True:
        msg = input('please input whatever you what say: ')
        if not msg:
            print('client closed')
            break
        print('input :{}'.format(msg))
        client_socket.send(msg.encode('utf-8'))
        resp = client_socket.recv(BUFF_SIZE)
        print('response:{}'.format(resp.decode('utf-8')))


if __name__ == '__main__':
    main()
