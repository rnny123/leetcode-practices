#first part of the code is to define the node class to create the nodes to store value
class Node:
    #define node but have prev and next for easy use later
    def __init__(self,key,value):
        self.key,self.val = key,value
        self.next = self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        #have max cap
        self.cap = capacity
        self.cache = {}

        #initialise the before and after empty nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right,self.left

    def remove(self,node):
        #remove from the left
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev


    def add(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #usage of this function is to 
        #1 get the key in the value but also put it to the right (to take note that it is most used)
        if key in self.cache:
            #this gets the whole node
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        #remove from the list (if exit length of cap)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)