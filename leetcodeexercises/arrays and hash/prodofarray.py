def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = [1] * len(nums)

    #first part of algo is to find the prefix value and store it in answer
    refix = 1
    #refix stores previous value
    for i in range(len(nums)):
        answer[i] = refix
        #store previous value
        refix *= nums[i]
    print(answer)

    #now same algo but now is to find postfix value
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        answer[i] = postfix*answer[i]
        postfix*=nums[i]
    return answer






answer = productExceptSelf([1,2,3,4])
print(f"answer = {answer}")
