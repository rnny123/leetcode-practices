class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    temp = head
    count = 0
    while head:
        count+=1
        head = head.next
    if k == 0  or count ==0:
            return temp
    times = k % count
    if times ==0:
        return temp

    value = ListNode(0)
    value.next = temp
    current = value.next
    prev = value
    for i in range(count-times):
        current = current.next
    return_v = current
    while current and current.next:
        current = current.next
    add = prev.next
    while prev.next != return_v:
        prev = prev.next
    prev.next = None
    current.next = add
    return return_v

head = [1,2,3,4,5]
k = 10
object = ListNode()
temp = object
for values in head:
    object.next = ListNode(values)
    object = object.next
answer = rotateRight(temp.next,k)
while answer:
    print(answer.val)
    answer = answer.next


