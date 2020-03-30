#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 98, 图5-2 TCP回射服务器——server
"""
import os
import time
import socket

BUFF_SIZE = 1024
PORT = 3000


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  s.bind(('', 3000)) specifies that the socket is reachable by any address the machine happens to have.
    server_socket.bind(('', PORT))
    server_socket.listen(5)  # backlog 5
    while True:
        connected_socket, addr = server_socket.accept()
        pid = os.fork()
        if pid == 0:  # 子进程
            print('I am child')
            server_socket.close()
            print('connecting from {}'.format(addr))
            str_echo(connected_socket)
            connected_socket.close()
            exit(0)
        else:  # 父进程
            print('I am father')
            connected_socket.close()


def str_echo(connected_socket):
    msg = connected_socket.recv(BUFF_SIZE)
    while len(msg) > 0:
        connected_socket.send(msg)
        msg = connected_socket.recv(BUFF_SIZE)
    print('end child, msg:{}'.format(msg))


if __name__ == '__main__':
    main()
