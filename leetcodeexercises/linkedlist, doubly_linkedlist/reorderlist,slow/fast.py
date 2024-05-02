class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    temp = head
    slow,fast = head,head.next

    #part 1 of algorithm: is to find the middle point. (using the slow/fast method)\
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    

    cur_node = slow.next
    slow.next = None
    prev_node = None
    

    
    
    #part 2: reverse the second part of the list
    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node

    #two pointer approach
    p1,p2 = head,prev_node
    while p2:
        next_p2 = p2.next
        next_p1 = p1.next
        p2.next = next_p1
        p1.next = p2
        p1 = next_p1
        p2 = next_p2
    return head

list = [1,2,3,4,5]
1>2>3>5>4
ll = ListNode(0)
ll2 = ll
for values in list:
    ll.next = ListNode(values)
    ll = ll.next

result_list = reorderList(ll2.next)

while result_list:
    print(result_list.val)
    result_list = result_list.next
