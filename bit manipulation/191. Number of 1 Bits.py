# EASY
# https://leetcode.com/problems/number-of-1-bits/description/

# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Approach using AND Bit Manipulation

def hammingWeight(n):
    count = 0

    while n > 0:
        n = n & (n-1)
        count += 1
    return count

# the n = n & (n-1) moves the right most set bit to 0 and all the others on the left get flipped. 