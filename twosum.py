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

value = twoSum([2,7,11,15], 9)
print(f"answer is {value}")