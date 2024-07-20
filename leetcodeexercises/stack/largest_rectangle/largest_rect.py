class Solution:
    def checkarea(self, stack, i, heights, area):
        index = stack.pop()
        value = heights[index]
        width = i if not stack else (i - stack[-1] - 1)
        curr_area = value * width
        print(f"stack = {stack}, i = {i}, index = {index}, value = {value}, width = {width}, area = {curr_area}")
        return(max(area, curr_area))
    def largestRectangleArea(self, heights):
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                area = self.checkarea(stack,i, heights, area)
            stack.append(i)
        
        # Handle remaining elements in the stack
        while stack:
            area = self.checkarea(stack, len(heights), heights, area)
        return area

heights = [2,1,5,6,2,3]
results = Solution().largestRectangleArea(heights)
print(f"the max height = to {results}")

