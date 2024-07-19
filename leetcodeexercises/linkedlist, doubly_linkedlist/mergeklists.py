class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #algo is to constantly split the list and merge them
        #time complex is log(n) because of the splitting of the lists
        if not lists and len(lists) <1:
            return None
        #basic handling of edge cases

        while len(lists) >1:
            #constantly merge until 1 lists is left
            mlists = []
            #list that stores the mergedlists. and it basically constantly resets every time we combine
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1<len(lists) else None
                #ensures that i+1 is in range
                mlists.append(self.mergelist(list1,list2))
                #combine the lists evenly and append it to the list called mergedlist
            lists = mlists
            #update lists to be the merge list array that you have created
        return lists[0]
        #return the 1st item of the lists[mergedlist (mlists)] basically the object you want

    def mergelist(self, list1, list2):
        #basic algo to merge the lists together
        start = ListNode()
        dummy = start
        while list1 and list2:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next
        if list1:
            start.next = list1
        if list2:
            start.next = list2
        return dummy.next

        