#practice instructions:
#to reverse the nodes from left to right

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    start = ListNode(0)
    start.next = head
    prev = start
    # same thing must initalise from start to 0 so it can account for complete reversal of whole linkedlist

    for i in range(left-1):
        prev = prev.next
    # go to the point to the point before the first node to reverse

    current_node = prev.next
    #initialise the current node and the next node

    for i in range(right-left):
        #reverse the rest of the linkedlist up to right
        next_node = current_node.next
        current_node.next = next_node.next
        next_node.next = prev.next
        #key point here: never change the current node, so for multiple reversals:
        #good to use prev.next to ensure that u always talking about the current node at the start of the reversal
        prev.next = next_node
    return start.next

list = [1,2,3,4,5]
left = 2
right = 4

linklist = ListNode(0)
linklist2 = linklist
for values in list:
    linklist.next = ListNode(values)
    linklist = linklist.next

answer = reverseBetween(linklist2.next,left,right)
while answer:
    print(answer.val)
    answer = answer.next

