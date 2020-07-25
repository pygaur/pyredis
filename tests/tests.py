"""
"""
import unittest

from smartcache.redis_communicator import SmartCache

import redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=2, socket_timeout=2)


class Tests(unittest.TestCase):
    """
    """

    def test_set(self):
        """
        :return:
        """
        with SmartCache() as cache:
            cache['test_1'] = 'str'
            cache['test_2'] = b'bytes'
            self.assertEqual(cache['test_1'], b'str')
            self.assertEqual(cache['test_2'], b'bytes')

