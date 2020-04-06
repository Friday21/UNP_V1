#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 538, 图26-2 TCP回射服务器（线程）——client
"""
import socket
import select
import sys
import threading

# HOST = '10.242.146.194'
HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024


def main():
    client_socket.connect((HOST, PORT))
    str_cli()


def str_cli():
    x = threading.Thread(target=copyto)
    x.start()
    while True:
        resp = client_socket.recv(BUFF_SIZE)
        print('resp is None:{}'.format(resp is None))
        print('response:{}'.format(resp.decode('utf-8')))
        if not resp:
            break


def copyto():
    while True:
        msg = input('please input whatever you what say: ')
        if not msg:
            print('client closed')
            break
        print('input :{}'.format(msg))
        client_socket.send(msg.encode('utf-8'))
    client_socket.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main()
