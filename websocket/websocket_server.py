#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-09-14 01:58
@Author  : Jann
@Contact : l33klin@gmail.com
@Site    : 
@File    : websocket_server.py
@Desc    : Description
"""
# WS server example

import time
import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"
    time.sleep(2)

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
