#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 538, 图26-2 TCP回射服务器（线程）——server
"""
import socket
import threading


BUFF_SIZE = 1024
PORT = 3000


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  s.bind(('', 3000)) specifies that the socket is reachable by any address the machine happens to have.
    server_socket.bind(('', PORT))
    server_socket.listen(5)  # backlog 5
    while True:
        connected_socket, addr = server_socket.accept()
        print('main thread got connected, fileno:{}'.format(connected_socket.fileno()))
        x = threading.Thread(target=str_echo, args=(connected_socket, ))
        x.start()


def str_echo(conn_socket):
    # 这里conn_socket函数的传递时线程安全的
    msg = conn_socket.recv(BUFF_SIZE)
    while len(msg) > 0:
        conn_socket.send(msg)
        msg = conn_socket.recv(BUFF_SIZE)
    print('end child-{}, msg:{}'.format(conn_socket.fileno(), msg))
    conn_socket.close()


if __name__ == '__main__':
    main()
