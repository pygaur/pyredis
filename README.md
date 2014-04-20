pyredis
=======

A python api to interact with redis .It implements all redis data structures and method. 
Useful to seperate calling redis connection to each place in any projects .


How to Use :
import SmartCache object into your file.
<pre>
>>>from smartcache.redis_communicator import SmartCache
</pre>

1 : hset :
<pre>
>>>cache = SmartCache()
>>>cache[('test', 'key'] = "value"
>>>True
</pre>


2 : hget
<pre>
>>>cache = SmartCache()
>>>out = cache[('test', 'key')]
>>>'value'
</pre>

3 : exists
<pre>
>>>cache = SmartCache()
>>>'test' in cache
>>>True
</pre>


4 : hexists
<pre>
>>>cache = SmartCache()
>>>('test', 'key') in cache
>>>True
</pre>

5 : sadd and smembers 
<pre>
>>>cache = SmartCache()
>>>cache['one'] = 'data'   # sadd
>>>cache['one']            # smembers
>>>(['data'])
>>>cache['one'] = 'data1'  #sadd
>>>cache['one']            # smembers
>>>set(['data', 'data1'])
</pre>

 
 

