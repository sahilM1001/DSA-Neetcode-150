# MEDIUM
# https://leetcode.com/problems/sum-of-two-integers/description/

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Input: a = 1, b = 2
# Output: 3

# Approach

def getSum(a, b):
    mask = 0xFFFFFFFF      # To keep numbers in 32-bit two's complement
    max_int = 0x7FFFFFFF   # 2**31 - 1
    min_int = 0x80000000   # 2**31
    while b != 0:
        a_masked = a & mask # masking to kep number inside 32-bit window
        b_masked = b & mask # masking to kep number inside 32-bit window
        temp_a = a_masked ^ b_masked # a XOR b results in carry 
        b = (a_masked & b_masked) << 1
        a = temp_a

    return a if a<= max_int else ~(a^mask)