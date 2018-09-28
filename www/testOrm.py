#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Gen Ye'

import orm
import asyncio

from models import User,Blog,Comment

async def test(loop):
    await  orm.create_pool(loop,user='www-data', password='www-data', db='elublog')

    u=User(name='Test',email='test2@126.com',passwd='123456',image='about:blank')

    await u.save()


if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test completed!')
    loop.close()

