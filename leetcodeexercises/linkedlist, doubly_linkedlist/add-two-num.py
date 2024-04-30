class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverselist(head):
    prev,current = None,head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def addTwoNumbers(l1, l2):
      """
      :type l1: ListNode
      :type l2: ListNode
      :rtype: ListNode
      """
      value1 = 0
      value2 = 0
      l1 = reverselist(l1)
      l2 = reverselist(l2)
      while l1:
          value1 = value1 * 10 + l1.val
          l1 = l1.next
          print(f"the value is:{value1}")
      while l2:
          value2 = value2 * 10 + l2.val
          l2 = l2.next
      print(f"value1: {value1}")
      print(f"value2 : {value2}")
      final = value1 + value2
      print(f"final value is {final}")
      dummy = ListNode()
      rtype = dummy
      if final == 0:
          rtype.next = ListNode(0)
      while final > 0:
          rtype.next = ListNode(final % 10)
          final = final // 10
          rtype = rtype.next
      return dummy.next

yeet = [2,4,9]
hi = [5,6,4,9]
dummy1 = ListNode()
dummy2 = ListNode()
l1 = dummy1
l2 = dummy2
for i in range(len(yeet)):
  l1.next = ListNode(yeet[i])
  l1 = l1.next
for i in range(len(hi)):
  l2.next = ListNode(hi[i])
  l2 = l2.next
result = addTwoNumbers(dummy1.next,dummy2.next)
while result is not None:
    print(result.val)
    result = result.next