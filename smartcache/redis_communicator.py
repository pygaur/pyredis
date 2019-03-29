"""
"""
import redis

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


class SmartCache(object):
    """
    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, socket_timeout=2)


    def __getitem__(self, key):
        """

        :param key:
        :return:
        """
        if isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            return self.red.hget(name, _key)

        if isinstance(key, str):
            return self.red.get(key)

    def __setitem__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        if isinstance(key, tuple):
            name = key[0]
            _key = key[1]
            self.red.hset(name, _key, value)

        else: # TODO --> key is string/int/byte only
            if isinstance(value, tuple):
                #  TODO -->  handle value[0] not int/byte/string
                self.red.set(key, *value) # TODO handle this much smart way. https://redis.io/commands/set
            else:
                #  TODO -->  handle value not int/byte/string
                self.red.set(key, value)  # TODO

    def __contains__(self, key):
        """
        key in cache
        (key, value) in cache
        :param key:
        :return:
        """
        if isinstance(key, tuple):
            _key = key[0]
            value = key[1]
            return self.red.hexists(_key, value)

        if isinstance(key, str):
            return self.red.exists(key)
