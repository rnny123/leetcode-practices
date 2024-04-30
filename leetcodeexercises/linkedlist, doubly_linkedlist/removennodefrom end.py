class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ph = ListNode()
        ph.next = head
        first = ph
        second = ph
        #creation of new listnode() object that starts with listnode(0) to account for cases when n and len of ll = 1
        #initialise two values that is equal to it so you can operate on this two linkedlsit
        
        for i in range(n+1):
            first = first.next
        #basically goes to the next value till i
        #if n = 2, go 2 value down
        
        while first:
            first = first.next
            second = second.next
            #move both pointers
            #ensures difference btwn is n
            #while first ensures u do until first is none (checks correctly that u remove the nth node)
        
        second.next = second.next.next
        #change the link
        #change the value of next to the following node
        #this skips/delete that node
        return ph.next
        #returns listnode(0).next, returning the original list (wanted)