print("hello world")

def threeSum(nums):
    nums.sort()
    answer = []
    for i in range(len(nums) -2):
        print(f"\ni = {i}")
        j = i+1
        k = len(nums) -1
        while j<k:
            value = nums[i] + nums[j] +nums[k]
            print(f"value = {value}, nums[i] = {nums[i]}, numsj = {nums[j]}, numsk = {nums[k]}")
            if value ==0:
                set = [nums[i],nums[j],nums[k]]
                if set not in answer:
                  
                    answer.append([nums[i],nums[j],nums[k]])
                j+=1
            if value<0:
                j +=1
            else:
                k -=1
    return answer

            

nums = [-2,0,1,1,2]
nums.sort()
print(nums)
print(threeSum(nums))

            
            
                

