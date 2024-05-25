class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.use = {}
        self.time = 0  # This will act as a simple clock.

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.time += 1
        self.use[key] = self.time  # Update last used time
        return self.cache[key]
    
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time += 1
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used
                least_used = min(self.use, key=self.use.get)  # Get least recently used key
                del self.cache[least_used]
                del self.use[least_used]

        self.cache[key] = value
        self.use[key] = self.time  # Update or set last used time

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
