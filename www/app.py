'''
@project: elublog
@author: Gen Ye
@datetime: 2018/9/27
Web 骨架
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1> Elublog </h1>',content_type='text/html',charset='utf-8')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv= yield from loop.create_server(app.make_handler(),'192.168.216.128',5000)
    logging.info('server started at http://192.168.216.128:5000...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()