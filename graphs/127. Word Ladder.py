# HARD
# https://leetcode.com/problems/word-ladder/description/

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if end word is not in wordlist, we cannot reach there so return 0
        if endWord not in wordList:
            return 0
        map_1 = defaultdict(list) # create a dict with val type of List []
        
        wordList.append(beginWord) # add begin word to wordlist

        for word in wordList:
            # for every word in wordList, 
            # iterate over the word, slice it at each index to create new patterns
            # suppose word is hit, the below loop will create patterns like 
            # *it, h*t, hi* 
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                map_1[pat].append(word)
        
        vis = set([beginWord]) # init visited set with beginning word
        
        q = deque([beginWord]) # init q with beginning word
        count = 1 # init answer with 1 
        while q:
            # while q
            for i in range(len(q)):
                # explore all children for the current level
                node = q.popleft() # pop a word
                if node == endWord:
                    # if popped word == end word, return count
                    return count
                for i in range(len(node)):
                    # create all patterns of the current word
                    pat = node[:i] + "*" + node[i+1:]
                    for neighbor in map_1[pat]:
                        # explore all neighbors of each pattern in the map,
                        # and add them to visited set if they are not visited
                        # also append the neighbor to q
                        if neighbor not in vis:
                            vis.add(node)
                            q.append(neighbor)
                    map_1[pat] = [] # mark pattern as [], so its not processed in the future
            count+=1 # increment count after completion of level
            
        return 0 # return 0 if we cannot reach the word