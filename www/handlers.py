#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Gen Ye'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    summary = '我的第一条博客。 Blog的创建日期显示的是一个浮点数，因为它是由这段模板渲染出来的：.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

# @get('/api/users')
# def api_get_users(*,page='1'):
#     page_index=get_page_index(page)
#     num=yield from User.findNumber('count(id)')
#     p=Page(num,page_index)
#     if num==0:
#         return dict(page=p,users=())
#     users=yield from User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
#     for u in users:
#         u.passwd='*******'
#         return dict(page=p,users=users)
@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)