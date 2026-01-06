# MEDIUM
# https://leetcode.com/problems/multiply-strings/description/

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Approach

def multiply(num1, num2):
    if "0" in [num1, num2]:
        return "0"
    # create array of len num1 + num2 with all places as zero, as the multiplication of any two numbers
    # cannot be greater than the length of num1 + num2
    res = [0] * (len(num1) + len(num2)) 
    num1, num2 = num1[::-1], num2[::-1] # reverse the strings as every multiplication starts from right most digit to left most ( units place to ones to hunderds place and so on)
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit = int(num1[i]) * int(num2[j]) # multiply individual number

            res[i + j] += digit # add the digit to res[i+j]
            
            res[i + j + 1] += res[i + j] // 10 # add the carry to res[i + j + 1] 
            res[i + j] = res[i + j] % 10 # update res[i + j] to remainder of digit calculated above
            
    res, beg = res[::-1], 0 # reverse res
    while beg < len(res) and res[beg] == 0: 
        beg += 1 # increment till res[i] != 0
    res = [str(x) for x in res[beg:]] # convert each int in the slice array res[i:] where res[i] != 0
    return "".join(res) # iterate over res and return the string ans