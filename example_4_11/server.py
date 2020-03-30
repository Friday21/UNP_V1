#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 89, 图4-11 显示客户IP地址和端口号的时间获取服务器程序
"""
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
        print('connecting from {}'.format(addr))
        msg = 'now time is:{}s'.format(int(time.time()))
        connected_socket.send(msg.encode('utf-8'))
        connected_socket.close()


if __name__ == '__main__':
    run()
