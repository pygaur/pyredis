pyredis
=======

A Python API to interact with Redis. It implements common Redis data structures and methods. 
Useful to separate Redis connection handling from business logic in your projects.


## How to Use

Import the SmartCache object into your file:
<pre>
>>> from smartcache.redis_communicator import SmartCache
</pre>

### Hash Operations

1. hset (set a field in a hash):
<pre>
>>> cache = SmartCache()
>>> cache[('test', 'key')] = "value"
>>> True
</pre>


2. hget (get a field from a hash):
<pre>
>>> cache = SmartCache()
>>> out = cache[('test', 'key')]
>>> b'value'
</pre>

### Key Existence Checks

3. exists (check if a key exists):
<pre>
>>> cache = SmartCache()
>>> 'test' in cache
>>> True
</pre>


4. hexists (check if a field exists in a hash):
<pre>
>>> cache = SmartCache()
>>> ('test', 'key') in cache
>>> True
</pre>

### Set Operations

5. sadd and smembers (adding to a set and retrieving all members):
<pre>
>>> cache = SmartCache()
>>> cache['one'] = 'data'   # sadd
>>> cache['one']            # smembers
>>> {b'data'}
>>> cache['one'] = 'data1'  # sadd
>>> cache['one']            # smembers
>>> {b'data', b'data1'}
</pre>

### List Operations

6. Adding elements to a list:
<pre>
>>> cache = SmartCache()
>>> cache.rpush('mylist', 'first')  # Add to the end
>>> cache.rpush('mylist', 'second')
>>> cache.lpush('mylist', 'start')  # Add to the beginning
>>> cache['mylist']                 # Get all list elements
>>> [b'start', b'first', b'second']
</pre>

7. Removing elements from a list:
<pre>
>>> cache = SmartCache()
>>> cache.lpop('mylist')    # Remove from the beginning
>>> b'start'
>>> cache.rpop('mylist')    # Remove from the end
>>> b'second'
>>> cache['mylist']
>>> [b'first']
</pre>

## Configuration

By default, SmartCache connects to Redis at:
- Host: 127.0.0.1
- Port: 6379
- DB: 0

You can configure these values:
<pre>
>>> cache = SmartCache(host='redis.example.com', port=6380, db=1)
</pre>

## Context Manager Support

SmartCache can be used as a context manager to ensure proper cleanup:
<pre>
>>> with SmartCache() as cache:
...     cache['key'] = 'value'
...     print(cache['key'])
b'value'
</pre>


 

