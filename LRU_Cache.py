# Title: 146. LRU Cache
# Difficult: Medium
# Problem: https://leetcode.com/problems/lru-cache/description/

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end of the ordered dictionary (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists, update its value and move it to the end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used key (the first key in the ordered dictionary)
            self.cache.popitem(last=False)
        # Add the new key-value pair to the ordered dictionary
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
