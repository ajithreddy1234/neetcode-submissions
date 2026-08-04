class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v=self.cache.pop(key)
        self.cache[key]=v
        return v
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            vaa=next(iter(self.cache))
            del self.cache[vaa]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)