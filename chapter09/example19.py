#using the continue statement
s = 'C3H7'
total = 0 # The sun of the digits seen so far.
count = 0 # The number of the digits seen so far.
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = total +int(s[i])
    count = count +1
print("Total is : ", total,"Count is :",count)