class Node:
    
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val


class LRUCache:

    """
    Using double Linked List data structure and a hash map to retrieve the specific node
    """

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.map = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old = self.map[key]
            self.remove(old)
        node = Node(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            deleteNode = self.head.next
            self.remove(deleteNode)
            del self.map[deleteNode.key]
        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def add(self, node):
        prevEnd = self.tail.prev
        prevEnd.next = node
        node.prev = prevEnd
        node.next = self.tail
        self.tail.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)