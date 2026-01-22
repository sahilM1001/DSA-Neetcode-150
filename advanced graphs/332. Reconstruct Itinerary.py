# HARD
# https://leetcode.com/problems/reconstruct-itinerary/description/

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

# Approach
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map_1 = defaultdict(list)
        # create map of all outgoing tickets/edges from each node
        for src, dest in tickets:
            map_1[src].append(dest)
        # sort the outgoing ticket/edges so they are in lexicographically/alphabetical smallest order
        for key, val in map_1.items():
            map_1[key] = sorted(val)

        ans = [] #init ans
        def dfs(airport):
            while map_1[airport]:
                # while there are outgoing tickets for the current airport, pop its nearest ticket and run dfs
                next_src = map_1[airport].pop(0)
                dfs(next_src)
            # After exhausting all outgoing tickets, append the current airport to ans array,
            # we are building our itinerary/route in reverse order
            ans.append(airport)
        dfs("JFK") # start with JFK airport as given in question
        return ans[::-1] # reverse the ans list and return
        