def removeDuplicates(nums):
    i=1
    for j in range (1,len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i +=1
    return i


nums = [1,1,2]
value = removeDuplicates(nums)
print(f"value is {value}")
print(f"new nums = {nums}")

