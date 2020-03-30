#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Page 89, 图4-11 显示客户IP地址和端口号的时间获取对应的客户端程序
"""
import socket

HOST = '10.242.146.194'
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
