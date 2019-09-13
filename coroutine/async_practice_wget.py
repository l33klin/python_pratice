#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-09-14 01:51
@Author  : Jann
@Contact : l33klin@gmail.com
@Site    : 
@File    : async_practice_wget.py
@Desc    : Description
@Ref     : https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640
"""


import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()