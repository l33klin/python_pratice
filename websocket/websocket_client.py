#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2019-09-14 02:00
@Author  : Jann
@Contact : l33klin@gmail.com
@Site    : 
@File    : websocket_client.py
@Desc    : Description
"""

# WS client example

import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")


async def count_task():
    seconds = 0
    for _ in range(5):
        await asyncio.sleep(1)
        seconds += 1
        print("count: {}".format(seconds))

tasks = [hello(), count_task()]
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
