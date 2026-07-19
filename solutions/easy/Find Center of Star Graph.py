// Title: Find Center of Star Graph
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        return list(set(edges[0]).intersection(edges[1]))[0]

