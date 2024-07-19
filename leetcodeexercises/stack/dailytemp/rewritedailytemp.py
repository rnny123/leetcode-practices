class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Example 1:
		# Input: temperatures = [73,74,75,71,69,72,76,73]
		# Output: [1,1,4,2,1,1,0,0]
        
        stack = []
        res = [0] * len(temperatures)
        for i,value in enumerate(temperatures):
            while (stack and value > temperatures[stack[-1]]):
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res

temp = [73,74,75,71,69,72,76,73]
result = [1,1,4,2,1,1,0,0]
ans = Solution().dailyTemperatures(temp)
print(f"my ans for the case of {temp} is: {ans} while the correct ans is {result}")
            
            