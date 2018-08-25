class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.nodedict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodedict:
            node = self.nodedict.get(key)
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodedict:
            node = self.nodedict.get(key)
            self.remove(node)

        node = Node(key,value)
        self.add(node)
        self.nodedict[key] = node
        if len(self.nodedict) > self.capacity:
            node = self.tail.pre
            self.remove(node)
            del self.nodedict[node.key]

    def add(self, node):
        self.head.next.pre = node
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node

    def remove(self,node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))