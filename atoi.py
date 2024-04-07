def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        sign = 1
        value = 0
        if len(s) == 0:
            return 0
        while i<len(s) and s[i] == ' ':
            i +=1
        if i<len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                 sign = -1
            i +=1
        while i<len(s) and '0' <= s[i] <= '9':
            value = value*10 + int(s[i])
            i +=1
        if value*sign < -(2**31):
            return -2**31
        elif value*sign > 2**31 -1:
            return 2**31 -1
        return (value*sign)
        

value = myAtoi("words and 987")
print(f"value is {value}")
                 
              
        
                
        