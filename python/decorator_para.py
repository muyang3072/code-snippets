# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:30:55 2018

@author: imuyang
"""

#refer: expert python programming 2nd

#example 1 --- parameter checking

rpc_info = {}

def xmlrpc(in_ = (), out = (type(None),)):
    def _xmlrpc(function):
        func_name = function.__name__
        rpc_info[func_name] = (in_,out)
        def _check_types(elements,types):
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements,types))
            for index,couple in typed:
                arg,of_the_right_type = couple
                if isinstance(arg,of_the_right_type):
                    continue
                raise TypeError('arg #%d should be %s' % (index,of_the_right_type))
                
        def __xmlrpc(*args):
            checkable_args = args[1:]
            _check_types(checkable_args,in_)
            res = function(*args)
            if not type(res) in (tuple,list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res,out)
            return res
        return __xmlrpc
    return _xmlrpc

class RPCView:
    @xmlrpc((int,int))
    def meth1(self,int1,int2):
        print('received %d and %d' %(int1,int2))
        
    @xmlrpc((str,),(int,))
    def meth2(self,phrase):
        print('received %s' % phrase)
        return 12
    
#example 2 --- cache

import time
import hashlib
import pickle
cache = {}
def is_obsolete(entry,duration):
    return time.time() - entry["time"] > duration

def compute_key(function,args,kw):
    key = pickle.dumps((function.__name__,args,kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args,**kw):
            key = compute_key(function,args,kw)
            if (key in cache and not is_obsolete(cache[key],duration)):
                print("we got a winner")
                return cache[key]["value"]
            result = function(*args,**kw)
            cache[key] = {
                    "value":result,
                    "time":time.time()
                    }
            return result
        return __memoize
    return _memoize


#example 3 --- agent
class user(object):
    def __init__(self,roles):
        self.roles = roles
        
class Unauthorized(Exception):
    pass

def protect(role):
    def _protect(function):
        def __protect(*args,**kw):
            user = globals().get("user)
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args,**kw)
        return __protect
    return _protect





















