#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""预先派生进程——服务器
page 654
"""
import time
import socket
import os
import signal
from multiprocessing import Lock


BUFF_SIZE = 1024
PORT = 3000
PROCESS_NUM = 10
pids = []


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    server_socket.listen(10)  # backlog 5
    for i in range(PROCESS_NUM):
        pid = make_child(server_socket)
        pids.append(pid)
    signal.signal(signal.SIGINT, sig_int)

    while True:
        time.sleep(1)


def sig_int(*args):
    for pid in pids:
        os.kill(pid, signal.SIGTERM)
    while True:
        try:
            os.waitpid(-1, 0)
        except ChildProcessError:
            break
    exit(0)


def make_child(confd):
    pid = os.fork()
    if pid > 0:
        return pid
    child_main(confd)


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
    # total cost: 19.945202112197876s, errors:23
