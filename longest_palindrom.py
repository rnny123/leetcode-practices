

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        #going from the middle of the string s
        left = len(s) // 2
        right = left
        print(f"initial value of right : {right} and left is: {left}")
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            print("entering the loop")
            left -= 1
            right += 1
            
        print(f"left value is: {left}")
        print(f"right value is {right}")

longestPalindrome("abaab")
                
                        
                        
                                
                

        
                
                
            