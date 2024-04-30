class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class linkedlist(object):
    def __init__(self):
        self.head = None

    def append_list(self,value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def mergeists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = ListNode()
        #create new_list object which is of class ListNode()
        dummy = new_list
        #create dummy to store the list object and can return the .next value.
        while list2 and list1:
            #loop through both linkedlist
            if list1.val < list2.val:
                #check if list1.value lesser than list2.value 
                new_list.next = list1
                #store the next value in list1
                list1 = list1.next
                #go to the next value of list1
            else:
                #basically means that list2.value is equal to or lesser than list1.value
                new_list.next = list2
                #store the next value of new_list to be of list 2
                list2 = list2.next
                #go to the next value of list 2
            new_list = new_list.next
            #initialise the new_list to go the next value
        if list1:
            #if still have value in list1
            new_list.next = list1
            #add list1 to the end of new_list
        elif list2:
            new_list.next = list2
            #add list2 to the end of new_list
        return dummy.next
        #this basically returns the linkedlist. because dummy = listNode(0) and it links to the first legit value of the linkedlist
        #so doing this returns the start of the linkedlist

    
list1 = [1,2,4]
list2 = [1,3,4]
yo = linkedlist()
for values in list1:
    yo.append_list(values)
yo2 = linkedlist()
for values in list2:
    yo2.append_list(values)
hi = linkedlist().mergeists(yo.head,yo2.head)
while hi:
    print(hi.val)
    hi = hi.next

