def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    answer = 0
    i = 0
    while i <len(height)-1:
        j = i+1
        if height[j] < height[i]:
            k = i+1
            highest_height = height[k]
            k_value = k
            while k<len(height):
                if height[k] > highest_height:
                        highest_height = height[k]
                        k_value = k
                k+=1
            max_height = min(height[i],highest_height)
            while j<k_value and (max_height-height[j]) >=0:
                answer += max_height - height[j]
                j+=1
            i = j-1
        i +=1
    return answer
def two_pointertrap(height):
    # more efficient solution for this trap problem
    # proper and full usage of the two pointer solution
    left = 0
    right = len(height) -1
    #basic 2 pointer initialisation of pointers
    answer = 0
    #creates the variable answer which is the return value for total area.
    max_left = height[left]
    max_right = height[right]
    #initialise the original values of max_left and max_right
    while left<right:
        #logic of the code:
        #max height is restrained by the min of (max_left and max_right)
        #so depending on which one is higher u calculate from there
        #if max left lower, calculate from restraining side
        #if same, doesnt really matter
        print(f"max_left is {max_left}, max right is {max_right}")
        if max_left<max_right:
            #restraining side is the left
            answer += max_left - height[left]
            #add the water trapped
            left +=1
            max_left = max(height[left], max_left)
            #find the next max left value
        else:
            #restraining side is the right side/equal
            answer += max_right - height[right]
            right -=1
            max_right = max(height[right],max_right)
            #same, finding the next max right value
    return answer
height = [5,5,1,7,1,1,5,2,7,6]
value = two_pointertrap(height)
print(f"value = {value}")






        