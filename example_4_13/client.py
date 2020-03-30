#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 92, 图4-13 典型的并发服务器——client
"""
import socket

# HOST = '10.242.146.194'
HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024


def run():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    msg = 'hello, server'
    client_socket.send(msg.encode('utf-8'))
    result = []
    while True:
        data = client_socket.recv(BUFF_SIZE)
        result.append(data)
        if len(data) < BUFF_SIZE:
            break
    print(b''.join(result))


if __name__ == '__main__':
    run()
