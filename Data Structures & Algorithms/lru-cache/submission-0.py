class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.s=OrderedDict({})
        
        

    def get(self, key: int) -> int:
        if key in self.s:
            self.s.move_to_end(key)
            return self.s[key]
        else:
            return -1

    

        

    def put(self, key: int, value: int) -> None:
        if key in self.s:
            self.s.move_to_end(key)
        self.s[key]=value
        if len(self.s)>self.capacity :
            self.s.popitem(last=False)
        
