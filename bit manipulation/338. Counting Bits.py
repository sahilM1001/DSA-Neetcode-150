# EASY
# https://leetcode.com/problems/counting-bits/description/

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

def countBits(n):
        ans = [-1]*(n+1)

        for i in range(0, n+1):
            count = 0
            n = i
            # This loop counts the number of 1 bits in a number
            while n > 0:
                n = n & (n-1)
                count += 1
            ans[i] = count # update the ans[i] with count for that number
        return ans