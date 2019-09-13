#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-09-14 01:26
@Author  : Jann
@Contact : l33klin@gmail.com
@Site    : 
@File    : async_pratice.py
@Desc    : Description
@Ref     : https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640
"""


import threading
import asyncio


@asyncio.coroutine
def hello(i):
    print('Hello world! {} {}'.format(i, threading.currentThread()))
    yield from asyncio.sleep(1)
    print('Hello again! {} {}'.format(i, threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello(1), hello(2), hello(3), hello(4)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
