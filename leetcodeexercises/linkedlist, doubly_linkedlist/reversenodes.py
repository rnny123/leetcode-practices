#problem is to reverse every k node in the linkedlist
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #same thing create new node Null (to swap first group)
        answer = ListNode(0,head)
        prev_group = answer

        while True:
            k_node = self.get_knode(prev_group,k)
            if not k_node:
                break
            next_node = k_node.next
            #start the reversal of nodes
            prev,current= next_node, prev_group.next
            while current != next_node:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            #done with the reversal
            #now to settle the order of the next_node
            temp = prev_group.next
            prev_group.next = k_node
            prev_group = temp

        return answer.next
    
    def get_knode(self,curr_node,k):
        #this is to basically find the next node
        while curr_node and k>0:
            #this while statement is to account for groups when not enough. eg groups of 3 but last 1 only 1 left eg
            #in this case curr_node will be Null
            curr_node = curr_node.next
            k-=1
        return curr_node
    

head = [1,2,3,4,5]
k = 3
temp = ListNode(0)
input = temp
for values in head:
    input.next = ListNode(values)
    input = input.next

answer = Solution().reverseKGroup(temp.next,k)
while answer:
    print(answer.val)
    answer = answer.next