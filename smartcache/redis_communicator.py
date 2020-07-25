"""
"""
import redis


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
SOCKET_TIMEOUT = 2


class SmartCache(object):
    """
    """

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT,
                 db=REDIS_DB, socket_timeout=SOCKET_TIMEOUT):
        self.redis = redis.Redis(host=host, port=port, db=db,
                                 socket_timeout=socket_timeout)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.redis.close()

    def __getitem__(self, key):
        if isinstance(key, str) or isinstance(key, bytes):
            return self.redis.get(key)
        elif isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            return self.redis.hget(name, _key)

    def __setitem__(self, key, value):
        if isinstance(value, str) or isinstance(value, bytes):
            self.redis.set(key, value)
        elif isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            self.redis.hset(name, _key, value)

    def __contains__(self, key):
        if isinstance(key, tuple):
            _key = key[0]
            value = key[1]
            return self.redis.hexists(_key, value)

        if isinstance(key, str):
            return self.redis.exists(key)
