#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""测试服务器的并发特性"""
# 注： 用多进程的方式测试并发效果并不理想， 因为客户端本身进程的开销比较大， 大部分时间都耗费在这上边了，
# 而服务端的性能则只占总时间的一小部分， 可以尝试改用async io
import os
import socket
import time

HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024
error_cnt = 0


def main():
    global error_cnt
    for i in range(1000):
        pid = os.fork()
        if pid == 0:  # 子进程
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((HOST, PORT))
            msg = 'hello'
            client_socket.send(msg.encode('utf-8'))
            try:
                resp = client_socket.recv(BUFF_SIZE)
            except (ConnectionResetError, BlockingIOError):
                error_cnt += 1
                print('error')
                exit(0)
            print('resp:{}'.format(resp))
            exit(0)

    while True:
        try:
            os.waitpid(-1, 0)
        except ChildProcessError:
            break


if __name__ == '__main__':
    t1 = time.time()
    main()
    print('total cost: {}s, error:{}'.format(time.time() - t1, error_cnt))
