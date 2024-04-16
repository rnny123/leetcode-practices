def swap_list(index1,index2,list):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    return list
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    #logic: is to find where end of index stops increasing, sorts it then swap with the value before that index
    j = len(nums) -1
    i = j
    difference = max(nums) - min(nums)
    #first pointer j point at end of nums
    while 0<=j-1<len(nums) and nums[j-1] >= nums[j]:
        print(f"j is {j}")
        #so i basically stop the pointer when the next value is not larger (showing that the next permutation need change index j-1)
        j-=1
    next_value = nums[i]
    while (i>j-1):
        #logic to find the next highest value before the max value we see in descending order
        temp_diff = nums[i] - nums[j-1]
        #to find the next highest logic..
        if temp_diff <= difference and temp_diff >0:
            difference =  nums[i] - nums[j-1]
            next_value = nums[i]
        i-=1
    print(f"next value is {next_value}")
    #sort the list after the max value seen to the end
    nums[j::] = sorted(nums[j::])
    print(nums)
    #if j ==0 check for edge cases of same element eg [1,1] or only 1 element [1]
    if j == 0:
        list = nums
    else:
        print(f"next_value index is {nums[j::].index(next_value) + j}")
        #finds the index of the next highest value and swap it with the value before the highest
        list = swap_list(nums[j::].index(next_value) + j,j-1,nums)
    return list

list = nextPermutation([1])
print(f"next permutation is {list}")

        
            


        