class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

def addTwoNumbers(l1, l2):
      """
      :type l1: ListNode
      :type l2: ListNode
      :rtype: ListNode
      """
      value1 = 0
      value2 = 0

      while l1 is not None:
          value1 = value1 * 10 + l1.val
          l1 = l1.next
      while l2 is not None:
          value2 = value2 * 10 + l2.val
          l2 = l2.next
      final = value1 + value2
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
dummy = ListNode()
l1 = dummy
l2 = dummy
for i in range(len(yeet)):
  l1.next = ListNode(yeet[i])
  l1 = l1.next
for i in range(len(hi)):
  l2.next = ListNode(hi[i])
  l2 = l2.next
addTwoNumbers(l1,l2)
  