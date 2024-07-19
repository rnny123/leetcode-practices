class Solution(object):
    def carFleet(self, target, position, speed):
            values = set(zip(position,speed))
            values = [items for items in values]
            values.sort(reverse = True)
            stack = []
            for pos,sp in values:
                time_taken = (target - pos) / sp
                if not stack or time_taken > stack[-1]:
                    stack.append(time_taken)  
            return (len(stack))
		#should do it and check the time takens in reverse

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
target = 10
position = [6,8]
speed = [3,2]
yeet = Solution().carFleet(target, position, speed)
print(f"output is {yeet}")
            
            


        
        
        
        
        
        