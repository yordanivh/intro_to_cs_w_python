s = 'C3H7'
digit_index = -1 #This will be -1 until we find a digit
for i in range(len(s)):
    # If we find a digit
    if s[i].isdigit():
        digit_index = i
        break #this exets the loop

print(digit_index)