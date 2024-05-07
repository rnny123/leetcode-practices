def findDuplicate(nums):
    #hidden linkedlist cycle question
    """
    :type nums: List[int]
    :rtype: int
    """
    #identify that this is a linkedlist question
    #cycle linkedlist
    #2 nodes point to the same node

    #first part of algorithm: isto find the intersection
    slow = 0
    fast = slow
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        #move fast pointer 2 times faster than slow
        #understand that distance between start and slow pointer from answer is the same
        if slow == fast:
            break

    p3 = 0
    #iterate through from start and from current slow pointer to find intersection
    #remember distance from intersection is now the same

    while True:
        p3 = nums[p3]
        slow = nums[slow]
        if p3 == slow:
            break
    return p3


nums = [2,5,9,6,9,3,8,9,7,1]
answer = findDuplicate(nums)
print(f"answer is {answer}")

#in this eg 0>2>9>1>3>6>8>7>9
#notice that the cycle starts at 8 and the distance between 9 from 8 and 0 is the same
#1st part of algo: get to 8
#2nd part of algo: iterate to get 9

    