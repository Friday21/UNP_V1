#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""预先派生线程——服务器
page 672
"""
import time
import socket
import os
import signal
import threading
from threading import Lock


BUFF_SIZE = 1024
PORT = 3000
PROCESS_NUM = 60
pids = []


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen(10)  # backlog 5
    threads = []
    for i in range(PROCESS_NUM):
        x = threading.Thread(target=child_main, args=[server_socket])
        threads.append(x)
        x.start()
    for x in threads:
        x.join()


def child_main(confd):
    while True:
        lock.acquire()  # accept前加锁， 防止惊群
        conn_socket, addr = confd.accept()  # 阻塞
        lock.release()
        msg = conn_socket.recv(BUFF_SIZE)
        while len(msg) > 0:
            time.sleep(0.1)
            conn_socket.send(msg)
            msg = conn_socket.recv(BUFF_SIZE)
        conn_socket.close()


if __name__ == '__main__':
    lock = Lock()
    main()
    # total cost: 1.8270797729492188s, errors:0
