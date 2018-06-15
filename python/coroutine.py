# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:01:11 2018

@author: imuyang
"""
from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def write2mysql():
    data = yield
    print(data)
    pass

def crawl():
    write2mysql().send(1,2,3)
    pass