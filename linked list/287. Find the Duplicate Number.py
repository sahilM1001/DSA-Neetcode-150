# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Input: nums = [1,3,4,2,2]
# Output: 2

# Input: nums = [3,1,3,4,2]
# Output: 3

# Approach 1 using set
def findDuplicate(nums):
    s1 = set()
    for i in nums:
        if i in s1:
            return i
        s1.add(i)
    return -1

# Approach 2 
# Since every value is between 1 and n, each number corresponds to an index in the array (num - 1).
# We can use the array itself as a marking tool:

# When we see a number, we go to its corresponding index and flip the sign of the value there.
# If we ever visit an index that is already negative, it means we've visited this number before → it's the duplicate.

def findDuplicate( nums):
    for num in nums:
        idx = abs(num)-1
        if nums[idx] < 0 :
            return abs(num)
        nums[idx] *= -1
    return -1

# Approach 3
# Treat the array like a linked list, where each index points to the next index given by its value.
# Because one number is duplicated, two indices will point into the same chain, creating a cycle — exactly like a linked list with a loop.

# Using Floyd’s Fast & Slow Pointer technique:

# The slow pointer moves one step at a time.
# The fast pointer moves two steps at a time.
# If there’s a cycle, they will eventually meet.
# Once they meet, we start a new pointer from the beginning:

# Move both pointers one step at a time.
# The point where they meet again is the duplicate number (the entry point of the cycle).

def findDuplicate(nums) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow