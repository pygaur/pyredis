import unittest
import redis 

from redis_communicator import SmartCache
 
red = redis.Redis(host='127.0.0.1', port=6379, db=1)


class Tests(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_hexists(self):
        '''test hexists into'''
        cache  = SmartCache()                
        red.delete('test')
        self.assertEqual('test' in cache, False) 

    def test_hset_hget(self):
        '''test hget and hset '''
        cache = SmartCache()
        cache[('test', 'key')] = 'value'
        self.assertEqual(cache[('test', 'key')], 'value')


if __name__ == '__main__':
    unittest.main()
