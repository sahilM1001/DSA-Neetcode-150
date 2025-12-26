# EASY
# https://leetcode.com/problems/happy-number/description/

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):
    visit = set()
    while n not in visit:
        visit.add(n)
        n = sum_of_squares(n)
        if n == 1:
            return True
    return False
        
def sum_of_squares(n):
    num = [int(d) for d in str(n)]
    ans = 0
    for i in num:
        ans+=int(i)**2
    return ans