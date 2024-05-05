# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashmap = {None:None}
        #have none none in the case where random links to null

        curr = head
        #first part is to store the new nodes(create with the head values)
        while curr:
            copy_node = Node(curr.val)
            hashmap[curr] = copy_node
            curr = curr.next

        curr = head
        #second part is to make the links for the node
        while curr:
            copy_node = hashmap[curr]
            copy_node.next = hashmap[curr.next]
            copy_node.random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]
    
node = [[7,None],[13,0],[11,4],[10,2],[1,0]]


