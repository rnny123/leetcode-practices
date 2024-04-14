def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = abs((nums[-1] + nums[-2] + nums[-3]) - target)
        answer = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                value = nums[i]+nums[j]+nums[k] - target
                if abs(value)<=closest:
                    closest = abs(value)
                    answer = nums[i]+nums[j]+nums[k]
                if value<0:
                    j +=1
                else:
                    k-=1
        return answer

nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
value = threeSumClosest(nums,target)
print(f"value = {value}")
