int_roman = {
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M' 
}

def closest(value):
    diff = value
    for index in int_roman:
        difference = value - index
        if (difference<diff and difference>=0):
            diff = difference
            final_ans = index
    return final_ans

def intToRoman(num):

    """
    :type num: int
    :rtype: str
    """
    answer = ''
    while num>0:
        value_index = closest(num)
        num -= value_index
        charcter = int_roman[value_index]
        answer += charcter
    return answer


ans = intToRoman(58)
print(f"answer is {ans}")