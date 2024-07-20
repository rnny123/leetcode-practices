class Solution:
    def search(self, nums):
        start = 0
        end = len(nums) - 1
        while (start <= end):
            middle = start + (end - start) // 2
            # must add the start because end- start //2 calculates midpoint relative to start point ok??
            if (target > nums[middle]):
                start = middle + 1
            elif (target < nums[middle]):
                end = middle - 1
            else:
                return (middle)
        return (-1)