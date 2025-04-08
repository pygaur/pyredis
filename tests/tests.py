"""
Unit tests for the SmartCache class.
"""
import unittest

from smartcache.redis_communicator import SmartCache

import redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
TEST_DB = 15  # Use a different DB for tests to avoid conflicts

# Create test Redis connection
red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=TEST_DB, socket_timeout=2)


class Tests(unittest.TestCase):
    """
    Tests for SmartCache functionality
    """
    def setUp(self):
        """
        Set up test environment
        """
        # Clear the test database before each test
        red.flushdb()
        self.cache = SmartCache(db=TEST_DB)
        
    def tearDown(self):
        """
        Clean up after each test
        """
        red.flushdb()
        self.cache.redis.close()

    def test_string_operations(self):
        """
        Test string get/set operations
        """
        self.cache['test_1'] = 'str'
        self.cache['test_2'] = b'bytes'
        self.assertEqual(self.cache['test_1'], b'str')
        self.assertEqual(self.cache['test_2'], b'bytes')
        
    def test_hash_operations(self):
        """
        Test hash operations
        """
        self.cache[('hash', 'field1')] = 'value1'
        self.cache[('hash', 'field2')] = 'value2'
        
        self.assertEqual(self.cache[('hash', 'field1')], b'value1')
        self.assertEqual(self.cache[('hash', 'field2')], b'value2')
        
        # Test existence
        self.assertTrue(('hash', 'field1') in self.cache)
        self.assertFalse(('hash', 'nonexistent') in self.cache)
        
    def test_set_operations(self):
        """
        Test set operations
        """
        # First value creates a string
        self.cache['set_key'] = 'value1'
        # Second value converts to a set
        self.cache['set_key'] = 'value2'
        
        # Get should return a set
        result = self.cache['set_key']
        self.assertTrue(isinstance(result, set))
        self.assertEqual(result, {b'value1', b'value2'})
        
        # Add a third value
        self.cache['set_key'] = 'value3'
        result = self.cache['set_key']
        self.assertEqual(result, {b'value1', b'value2', b'value3'})
        
    def test_list_operations(self):
        """
        Test list operations
        """
        # Push to list
        self.cache.rpush('list_key', 'value1')
        self.cache.rpush('list_key', 'value2')
        self.cache.lpush('list_key', 'value0')
        
        # Test get
        result = self.cache['list_key']
        self.assertEqual(result, [b'value0', b'value1', b'value2'])
        
        # Test pop
        left = self.cache.lpop('list_key')
        right = self.cache.rpop('list_key')
        
        self.assertEqual(left, b'value0')
        self.assertEqual(right, b'value2')
        
        # Check remaining
        result = self.cache['list_key']
        self.assertEqual(result, [b'value1'])
        
    def test_existence(self):
        """
        Test key existence checks
        """
        self.cache['string_key'] = 'value'
        self.cache[('hash_key', 'field')] = 'value'
        
        self.assertTrue('string_key' in self.cache)
        self.assertTrue(('hash_key', 'field') in self.cache)
        self.assertFalse('nonexistent' in self.cache)
        
    def test_context_manager(self):
        """
        Test context manager functionality
        """
        with SmartCache(db=TEST_DB) as cache:
            cache['context_test'] = 'value'
            self.assertEqual(cache['context_test'], b'value')
            
        # Cache should still be accessible after context exit
        self.assertEqual(self.cache['context_test'], b'value')
        
        
if __name__ == '__main__':
    unittest.main()

