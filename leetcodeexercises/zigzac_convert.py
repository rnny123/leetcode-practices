def convert(s, numRows):
    if numRows == 1:
      return s
    result = [''] * numRows
    row = 0
    direction =1
    string = ''
    print(result)
    for i in range(len(s)):
        if row == (numRows-1):
           direction = -1
        elif row == 0:
           direction = 1
        result[row] += str(s[i])
        row += direction
        print(result)

    for i in range(numRows):
       for values in result[i]:
          string += values
    return(string)
          
          

str = convert("ABCDE", 4)
print(f"value is {str}")
