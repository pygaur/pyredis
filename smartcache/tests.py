"""
"""
import unittest

from redis_communicator import SmartCache

#  TEMP CODE #TODO Remove
import redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1, socket_timeout=2)
#  END code remove


class Tests(unittest.TestCase):
    """

    """

    def setUp(self):
        """
        """
        self.cache = SmartCache()
        red.flushall() # TODO fix this line.

    def test_set(self):
        """
        :return:
        """
        self.cache['test'] = 'VALUE'
        self.assertEqual(self.cache['test'], b'VALUE')

        self.cache['test1'] = b'VALUE'
        self.assertEqual(self.cache['test1'], b'VALUE')

        self.cache['test2'] = 1234.9
        self.assertEqual(self.cache['test2'], b'1234.9')

        self.cache['test3'] = 1234
        self.assertEqual(self.cache['test3'], b'1234')

        import pdb; pdb.set_trace()

    def test_set_invalid_cases(self):
        """
        :return:
        """
        self.skipTest(reason="Not Implemented.")

    def test_set_with_options(self):
        """
        :return:
        """
        self.cache['test_1'] = 1111, 1000, 1000
        self.assertEqual(self.cache['test_1'], b'1111')

    def test_set_EX(self):
        """
        :return:
        """
        self.skipTest(reason="Not Implemented.")

    def test_set_PX(self):
        """
        :return:
        """
        self.skipTest(reason="Not Implemented.")

    def test_set_NX(self):
        """
        :return:
        """
        self.skipTest(reason="Not Implemented.")

    def test_set_XX(self):
        """
        :return:
        """
        self.skipTest(reason="Not Implemented.")

if __name__ == '__main__':
    unittest.main()
