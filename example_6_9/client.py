#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 133, 图6-9 TCP回射服务器（I/O复用）——client
用select 同时监控client_socket和标准输入的可读状态
"""
import socket
import select
import sys

# HOST = '10.242.146.194'
HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    str_cli(client_socket)


def str_cli(client_socket):
    inputs = [sys.stdin, client_socket]
    close = False
    while not close:
        readable, writable, exceptional = select.select(inputs, [], [])
        for read_socket in readable:
            if read_socket is client_socket:
                print('client socket is readable')
                resp = client_socket.recv(BUFF_SIZE)
                print('response:{}'.format(resp.decode('utf-8')))
            else:
                print('stand input is ready')
                msg = input()
                # msg = read_socket.recv(BUFF_SIZE)
                if not msg:
                    close = True
                    print('client closed')
                    break
                print('input :{}'.format(msg))
                client_socket.send(msg.encode('utf-8'))


if __name__ == '__main__':
    main()
