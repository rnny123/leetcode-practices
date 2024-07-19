class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        results = []
        for values in heights:
            if stack and (stack[-1] <= values):
                stack.append(values)
                area = stack[0] * len(stack)
                results.append(area)
                stack = []
            else:
                stack.append(values)
        print(results)
        return max(results)
    
heights = [2,4]
results = Solution().largestRectangleArea(heights)
print(f"the max height = to {results}")

