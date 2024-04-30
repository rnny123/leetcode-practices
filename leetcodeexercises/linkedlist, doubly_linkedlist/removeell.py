# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    value = ListNode(0)
    value.next = head
    prev = value
    current = value.next
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next
    return value.next



val = 7
list = [7,7]
object = ListNode(0)
yeet = object
for values in list:
    object.next = ListNode(values)
    object = object.next

answer = removeElements(yeet.next,val)
while answer:
    print(answer.val)
    answer = answer.next