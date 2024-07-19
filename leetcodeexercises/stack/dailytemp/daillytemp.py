class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        count = 0
        stack = []
        res = [0] * len(temperatures)
        for index,temp in enumerate(temperatures):
            print(f"for count of {count}")
            count += 1
            while (stack and temperatures[stack[-1]] < temp):
                print(f"temp value is {temp} while current stack value is {temperatures[stack[-1]]}")
                i = stack.pop()
                print(f"value of i is {i}, index = {index}")
                res[i] = index - i
            stack.append(index)
        return (res)

[76,73]
[1,1,4,2,1,0,0,0]
temp = [71,76,72,51,63,1,3,5]
[3,4,6]
answer = [1,1,4,2,1,1,0,0]
res = Solution().dailyTemperatures(temp)
print(f"result is {res}\n answer is {answer}")

        
    
