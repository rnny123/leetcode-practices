def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    value = 0
    dict = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            }
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'I' and (i+1)<len(s) and (s[i+1] == 'X' or s[i+1]== 'V'):
            value -= dict['I']
        elif s[i] == 'X' and (i+1)<len(s) and (s[i+1] == 'L' or s[i+1]== 'C'):
            value -= dict['X']
        elif s[i] == 'C' and (i+1)<len(s) and (s[i+1] == 'D' or s[i+1]== 'M'):
            value -= dict['C']
        else:
            value += dict[s[i]]
    return value

value=romanToInt("CM")
print(f"value is {value}")