def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = len(nums) -1
    while i<j:
        if nums[i] < nums[j]:
            i +=1
        else:
            j-=1
        
            


        