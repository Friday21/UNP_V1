#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 92, 图4-13 典型的并发服务器——server
"""
import os
import time
import socket

PORT = 3000


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  s.bind(('', 3000)) specifies that the socket is reachable by any address the machine happens to have.
    server_socket.bind(('', PORT))
    server_socket.listen(5)  # backlog 5
    while True:
        connected_socket, addr = server_socket.accept()
        pid = os.fork()
        if pid == 0:  # 子进程
            print('I am child')
            print(server_socket.getsockname())
            server_socket.close()
            print('connecting from {}'.format(addr))
            msg = 'now time is:{}s'.format(int(time.time()))
            print('connected socket:{}'.format(connected_socket.getsockname()))
            connected_socket.send(msg.encode('utf-8'))
            connected_socket.close()
            print('child closed')
            exit(0)
        else:  # 父进程
            print('I am father')
            connected_socket.close()


if __name__ == '__main__':
    run()
