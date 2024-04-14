
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    value = []
    for i in range (len(nums)-3):
        for l in range(i+1,len(nums)-2):
            k = len(nums) - 1
            j = l+1
            while j <k:
                answer = (nums[i] + nums[l] + nums[j] + nums[k]) - target
                if  answer == 0:
                    answer1 = [nums[i],nums[l],nums[j],nums[k]]
                    if answer1 not in value:
                        value.append([nums[i],nums[l],nums[j],nums[k]])
                    j+=1
                elif (answer)<0:
                    j+=1
                else:
                    k-=1
    return value

nums = [1,0,-1,0,-2,2]
target = -3
answer = fourSum(nums,target)
print(f"answer is {answer}")