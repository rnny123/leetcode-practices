def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = [0 for i in range(len(nums))]
    #step 1 create array to store the values
    for i in range(len(nums)):
        times = 1
        for j in range(len(nums)):
            if j == i:
                pass
            else:
                times *= nums[j]
        answer[i] = times
    return answer



answer = productExceptSelf([-1,1,0,-3,3])
print(f"answer = {answer}")
