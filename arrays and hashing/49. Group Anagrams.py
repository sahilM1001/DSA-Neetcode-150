# MEDIUM
# https://leetcode.com/problems/group-anagrams/description/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

def groupAnagrams(self, strs):
        map_1 = {}

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in map_1:
                item = map_1[sorted_i]
                item.append(i)
                map_1[sorted_i] =  item
            else:
                map_1[sorted_i] = [i]
        arr = []
        for k, v in map_1.items():
            arr.append(v)
        return arr