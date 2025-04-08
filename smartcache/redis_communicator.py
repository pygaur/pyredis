"""
Redis wrapper providing a Pythonic interface for common Redis operations.
"""
import redis


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
SOCKET_TIMEOUT = 2


class SmartCache(object):
    """
    A Pythonic wrapper for Redis that provides a dictionary-like interface.
    Supports string, hash, set, and list operations through familiar Python syntax.
    """

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT,
                 db=REDIS_DB, socket_timeout=SOCKET_TIMEOUT):
        """
        Initialize Redis connection.
        
        Args:
            host: Redis host address
            port: Redis port
            db: Redis database number
            socket_timeout: Socket timeout in seconds
        """
        self.redis = redis.Redis(host=host, port=port, db=db,
                                 socket_timeout=socket_timeout)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.redis.close()

    def __getitem__(self, key):
        """
        Get values from Redis.
        
        If key is a string or bytes, get a string value.
        If key is a tuple of (name, field), get a hash field.
        If key is a set, return all set members.
        If key is a list, return all list elements.
        
        Returns:
            The value from Redis.
        """
        try:
            if isinstance(key, tuple):
                if len(key) != 2:
                    raise ValueError("Tuple key must have exactly 2 elements: (name, field)")
                name, field = key
                return self.redis.hget(name, field)
            else:
                # Check key type
                key_type = self.redis.type(key)
                if key_type == b'set':
                    return self.redis.smembers(key)
                elif key_type == b'list':
                    return self.redis.lrange(key, 0, -1)
                else:
                    return self.redis.get(key)
        except redis.RedisError as e:
            raise KeyError(f"Error accessing Redis: {str(e)}")

    def __setitem__(self, key, value):
        """
        Set values in Redis.
        
        If key is a tuple of (name, field), set a hash field.
        If key is a string/bytes and the key exists as a set, add to the set.
        Otherwise set a string value.
        """
        try:
            if isinstance(key, tuple):
                if len(key) != 2:
                    raise ValueError("Tuple key must have exactly 2 elements: (name, field)")
                name, field = key
                self.redis.hset(name, field, value)
            else:
                # Check if this is a set already
                key_type = self.redis.type(key)
                if key_type == b'set':
                    self.redis.sadd(key, value)
                elif key_type == b'none':
                    # For new keys, check if we should convert to set
                    # This implementation matches the README examples where
                    # assigning a second value to the same key converts it to a set
                    old_value = self.redis.get(key)
                    if old_value is not None:
                        # Convert string to set
                        pipe = self.redis.pipeline()
                        pipe.delete(key)
                        pipe.sadd(key, old_value)
                        pipe.sadd(key, value)
                        pipe.execute()
                    else:
                        # For new keys
                        self.redis.set(key, value)
                elif key_type == b'string':
                    # Convert string to set if a value already exists
                    old_value = self.redis.get(key)
                    if old_value is not None and old_value != value:
                        # Convert string to set
                        pipe = self.redis.pipeline()
                        pipe.delete(key)
                        pipe.sadd(key, old_value)
                        pipe.sadd(key, value)
                        pipe.execute()
                    else:
                        # Update existing string
                        self.redis.set(key, value)
                elif key_type == b'list':
                    # Add to list
                    self.redis.rpush(key, value)
                else:
                    # For existing string keys
                    self.redis.set(key, value)
        except redis.RedisError as e:
            raise KeyError(f"Error writing to Redis: {str(e)}")

    def __contains__(self, key):
        """
        Check if a key or field exists in Redis.
        
        If key is a tuple of (name, field), check if the hash field exists.
        If key is a string/bytes, check if the key exists.
        
        Returns:
            bool: True if the key/field exists, False otherwise.
        """
        try:
            if isinstance(key, tuple):
                if len(key) != 2:
                    raise ValueError("Tuple key must have exactly 2 elements: (name, field)")
                name, field = key
                return bool(self.redis.hexists(name, field))
            else:
                return bool(self.redis.exists(key))
        except redis.RedisError as e:
            raise KeyError(f"Error checking Redis: {str(e)}")
            
    def make_set(self, key):
        """
        Convert a Redis string to a set.
        
        Args:
            key: The key to convert
            
        Returns:
            bool: True if conversion was successful
        """
        try:
            key_type = self.redis.type(key)
            if key_type == b'string':
                old_value = self.redis.get(key)
                if old_value is not None:
                    pipe = self.redis.pipeline()
                    pipe.delete(key)
                    pipe.sadd(key, old_value)
                    pipe.execute()
                    return True
            return False
        except redis.RedisError as e:
            raise KeyError(f"Error converting to set: {str(e)}")
            
    def lpush(self, key, value):
        """
        Add an element to the beginning of a list.
        If the key does not exist, create a new list.
        
        Args:
            key: The list key
            value: The value to add
            
        Returns:
            int: Length of the list after the push
        """
        try:
            return self.redis.lpush(key, value)
        except redis.RedisError as e:
            raise KeyError(f"Error pushing to list: {str(e)}")
            
    def rpush(self, key, value):
        """
        Add an element to the end of a list.
        If the key does not exist, create a new list.
        
        Args:
            key: The list key
            value: The value to add
            
        Returns:
            int: Length of the list after the push
        """
        try:
            return self.redis.rpush(key, value)
        except redis.RedisError as e:
            raise KeyError(f"Error pushing to list: {str(e)}")
            
    def lpop(self, key):
        """
        Remove and return the first element of a list.
        
        Args:
            key: The list key
            
        Returns:
            The value of the first element
        """
        try:
            return self.redis.lpop(key)
        except redis.RedisError as e:
            raise KeyError(f"Error popping from list: {str(e)}")
            
    def rpop(self, key):
        """
        Remove and return the last element of a list.
        
        Args:
            key: The list key
            
        Returns:
            The value of the last element
        """
        try:
            return self.redis.rpop(key)
        except redis.RedisError as e:
            raise KeyError(f"Error popping from list: {str(e)}")
            
    def llen(self, key):
        """
        Get the length of a list.
        
        Args:
            key: The list key
            
        Returns:
            int: The length of the list
        """
        try:
            return self.redis.llen(key)
        except redis.RedisError as e:
            raise KeyError(f"Error getting list length: {str(e)}")
