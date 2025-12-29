# MEDIUM
# https://leetcode.com/problems/reverse-integer/description/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

# Approach

def reverse(self, x: int) -> int:
    new_num = 0
    min_num = -2 ** 31 # lower bound for valid num
    max_num = (2**31) -1 # upper bound for valid num
    new_n = abs(x) # converting to abs for easy digit extraction
    while new_n > 0:
        dig = new_n % 10 # getting last digit
        new_n = new_n // 10 # removing last digit from the number and making it smaller
        if ((new_num * 10) + dig) > max_num or -((new_num * 10) + dig) < min_num:
            return 0 # when new_num can overflow any lower/upper bound
        new_num *= 10 # shift the digits to left by multiplying with 10 and increasing their unit place
        new_num += dig # add the new digit to new_num
    return -new_num if x < 0 else new_num # return signed number