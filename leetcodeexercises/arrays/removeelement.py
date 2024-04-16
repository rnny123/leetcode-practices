def swapvalues(a,b, list):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums) - 1
        i = 0
        sum = 0
        for values in nums:
            if values == nums:
                sum +=1
        if sum == len(nums):
            nums = []
            return 0
             
        while i<= j:
            if nums[j] == val:
                j-=1
            elif nums[i] == val:
                swapvalues(i,j,nums)
                j-=1
                i+=1
            else:
                i +=1      
        return i

def easyremoveelement(nums,value):
    for answer in nums:
        if answer == value:
            print("yeet")
            nums.remove(answer)
            print(nums)
    return len(nums)


nums = [2,2,3]
value = 2
answer = easyremoveelement(nums,value)
print(f"new nums is {nums}")
print(f"answer is {answer}")

