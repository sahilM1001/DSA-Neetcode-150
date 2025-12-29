# EASY
# https://leetcode.com/problems/reverse-bits/description/


# Reverse bits of a given 32 bits signed integer.
# Input: n = 43261596
# Output: 964176192

# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Approach using Bit manipulation

def reverseBits( n):
    i = 0 
    new_num = 0 # init new num with zero
    while i < 32: # loop till 32 as we have 32 bit signed integer
        zero_or_one = n & 1 # n & 1 gives 0 when last bit is 0 and 1 when last bit is 1
        n = n >> 1 # right shifting n by 1 to drop the last bit
        new_num = new_num << 1 # left shifting new num by 1 to add one bit to it
        new_num = new_num | zero_or_one  # updating new num with the last bit extracted earlier using OR operation
        i+=1 # increasing loop
    return new_num #finally returning new num
    