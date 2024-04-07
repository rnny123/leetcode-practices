def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    answer = 0
    sign = 1

    if x < 0:
        sign = -1
        x = -x
    while x > 0:
        answer = (answer * 10) + x%10
        x = x // 10
    answer = answer * sign
    if answer < -2 ** 31 or answer > (2**31) -1:
        answer = 0
    return answer

value = 120
print(f"x is equal to {value}")
answer = reverse(value)
print(f"x is now equal to {answer}")
    
    