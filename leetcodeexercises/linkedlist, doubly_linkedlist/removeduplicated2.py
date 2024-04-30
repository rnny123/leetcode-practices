# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    start = ListNode(0)
    start.next = head
    prev = start
    middle = start.next
    while middle and middle.next:
        
        if current.val == current.next.val or current.val == current_value:
            current = current.next
        else:
            prev = prev.next
        current = current.next
        current_value = current.val
    return start

head = [1,1,1,2,3]
start = ListNode(0)
yeet = start
for values in head:
    start.next = ListNode(values)
    start = start.next

answer = deleteDuplicates(yeet.next)
while answer:
    print(f"value is {answer.val}")



        
        