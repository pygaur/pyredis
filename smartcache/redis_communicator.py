import redis 

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


class SmartCache(object):
    """
    python connector to implement redis methods and datatypes    
    """
 
    def __getitem__(self, key):
        red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, socket_timeout=2)
        if isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            return red.hget(name, _key)
        if isinstance(key, str):
            return red.smembers(key)

    def __setitem__(self, key, value):
        red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, socket_timeout=2)
        if isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            red.hset(name, _key, value)
        else:
            red.sadd(key, value)

    def __contains__(self, key):
        red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, socket_timeout=2)
        if isinstance(key, tuple):
            _key = key[0]
            value = key[1]
            return red.hexists(_key, value)
        if isinstance(key, str):
            return red.exists(key)

~                                   
