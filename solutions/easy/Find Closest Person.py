// Title: Find Closest Person
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/find-closest-person/

    def findClosest(self, x, y, z):
        count = [abs(x - z), abs(y - z)]
        if count[0] == count[1]:
            return 0 
        if count[0] < count[1]:
            return 1
        else:
            return 2
class Solution(object):
