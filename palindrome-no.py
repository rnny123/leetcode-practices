def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    is_true = False
    count = 0

    str_x = str(x)
    for i in range(len(str_x)):
        if (str_x[i] == str_x[len(str_x) - 1 -i]):
            count +=1
    if count == len(str_x):
        is_true = True
    return is_true


        
value = isPalindrome(10)
print(f"is it a palindrome: {value}")                  