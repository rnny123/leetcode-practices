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


nums = [2,3,4,5]
value = 2
answer = easyremoveelement(nums,value)
print(f"new nums is {nums}")
print(f"answer is {answer}")

def swap(i1,i2,array):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp
    

#so function removes 1st instance of value
def easyremoveelement2(nums,value):
	while (i < len(nums)):
          if nums[i] == value:
               while (i+1 < len(nums)):
                    swap(i,i+1,nums)
                    i += 1
        i+= 1
    nums.pop()
    return len(nums)

yeet = [2,3,4,5]
[3,2,4,5]
[3,4,2,5]
[3,4,5,2]
easyremoveelement2(yeet,2)
print(f"new value of yeet = {yeet}")