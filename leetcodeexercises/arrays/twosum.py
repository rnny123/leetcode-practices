def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index,value in enumerate(nums):
            dict[value] = index
        for index,value in enumerate(nums):
            needed = target - value
            if (needed in dict) and (dict[needed] != index):
                return ([index, dict[needed]])
        return NULL
def twosum2P(nums,target):
    yeet = nums.copy()
    nums.sort()
    left = 0
    right = len(nums) -1
    while left<right:
        value = nums[left] + nums[right]
        print(nums)
        print(yeet)
        if value == target:
            if yeet.index(nums[left]) == yeet.index(nums[right]):
                return
            return ([yeet.index(nums[left]),yeet.index(nums[right])])
        elif value > target:
            right -=1
        else:
            left +=1

        
         

value = twosum2P([3,3], 6)
print(f"answer is {value}")