class Node:
    #class node: creates a class to store a value of linkedlist with attributes value and next
    def __init__(self,value):
        #initialise the value of value and next (attributes)
        self.value = value
        self.next = None

class Linkedlist:
    #class linkedlist: single link linkedlist (a points to b etc)
    def __init__(self):
        self.head = None
        #initialise linkedlist to have a start/head value of None

    def insert_at_front(self,value):
        #method, that insert next value to the front
        new_node = Node(value)
        #create new_node based on value. new_node has attributes value and next (now new_node.next = 0)
        new_node.next = self.head
        #link new_node to the original list
        self.head = new_node
        #now make the new_node as the head of the list, after the links have been made


    def append(self,value):
        #addition of new Nodes to the back of the linked list
        new_node = Node(value)
        #same thing: create a node from value to give it the attributes value and next
        if not self.head:
            #if its the first value assign, make the value the head.
            self.head = new_node
        else:
            current_node = self.head
            #current node that you are on
            while current_node.next:
                #basically ensuring it goes to the end of the linkedlist
                #this is the logic: while current_node.next ensure the linkedlist is looped to the last value
                #for eg for linkedlist 1>2>3>4>5, current value of list.head.value is 5, because the loop stops at 5 as list.next = None
                current_node = current_node.next
                #go to the next value
            current_node.next = new_node
            #link the last value/ node to the new_node that u pass in this method (in the above eg:5)
    
    def display(self):
        #method to display the current values in the linkedlist
        while self.head:
            #while .head has a value so it will enter the loop up to 5, when self.head.value =5
            print(f"current value is {self.head.value}")
            #print the value of the head
            self.head = ll.head.next
            #go to the next node

    def remove_index(self,index):
        #method to remove value at the index numerical value i pass in
        if index <0:
           #error handling 1: check if input value of index is more than 0, if it is less it is invalid and a higher value is required
           print("sorry :( index must be greater than 0")
           return
        elif index == 0:
            #error handling 2, if index ==0, so it does a different algorithm den if it is more than 0
            # it also checks if your linkedlist is created cause if it is not it will enter the error message
            if self.head:
                self.head = self.head.next
            #if you remove the first value of the linkedlist, the next value now becomes the head of the linkedlist
            else:
                #error message to print if error of linkedlist not present is occured
                print("sorry bro, your linkedlist not created, please create the linkedlist")
                return
        else:
            #enters this if index is valid and linked list is present
            current_value = self.head
            for i in range(index-1):
                #enters the for loop until the value before the index you want to remove
                if not current_value:
                    #if index input value is out of the range
                    print("sorry brooooo out of range of linkedlist")
                    return
                current_value = current_value.next
            #double checks if input index value is out of range
            if not current_value or not current_value.next:
                print("sorry brooooo out of range of linkedlist")
                return
            #links the value before the index to remove to the next value after the index to be remove
            next_value = current_value.next
            current_value.next = next_value.next



list = [1,2,3,4,5]
ll = Linkedlist()
for values in list:
    ll.append(values)
ll.remove_index(238923)
ll.display()


    
        




        