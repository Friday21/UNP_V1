#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试服务器的并发特性--asyncio 版本"""

import asyncio
import socket
import time

HOST = '127.0.0.1'
PORT = 3000
BUFF_SIZE = 1024
error_cnt = 0


async def main():
    loop = asyncio.get_event_loop()
    futures = []
    for i in range(1000):
        future = loop.run_in_executor(None, str_cli)
        futures.append(future)
    for f in futures:
        resp = await f
        print(resp)


def str_cli():
    global error_cnt
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    msg = 'hello'
    try:
        client_socket.send(msg.encode('utf-8'))
        resp = client_socket.recv(BUFF_SIZE)
    except (BrokenPipeError, BlockingIOError, ConnectionResetError) as e:
        error_cnt += 1
        return 'error'
    return resp


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('total cost: {}s, errors:{}'.format(time.time() - t1, error_cnt))
