# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    list = ListNode(0)
    list.next = head
    temp = list

    while temp and temp.next and temp.next.next:
        first = temp.next
        second = temp.next.next

        temp.next = second
        first.next = second.next
        second.next = first

        temp = temp.next.next

    return list.next

linkedlist = ListNode(0)
list = [1,2,3,4]
temp = linkedlist
for values in list:
    linkedlist.next = ListNode(values)
    linkedlist = linkedlist.next

answer = swapPairs(temp.next)
while answer:
    print(answer.val)
    answer = answer.next

        