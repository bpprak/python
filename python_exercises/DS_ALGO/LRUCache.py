from collections import deque
class LRUCache:
    
    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()
    
    # just to remove from one position and add in to front and finally return the value    
    def get(self, key: int) -> int:
        if(key in self.m):
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1
    #if the key already exist then remove from that place and place it in front
    #if the key not present then remove existing last element and add the new element in to front.    
    def put(self, key: int, value:int) -> None:
        if key not in self.m:
            if len(self.deq) == self.c:                
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)
        
        self.m[key] = value
        self.deq.append(key)

Object = LRUCache(4)


print(Object.put(1,10))
print(Object.put(2,11))
print(Object.put(3,15))
print(Object.put(4,26))

print(Object.put(3,12))
print(Object.deq)
print(Object.m)

