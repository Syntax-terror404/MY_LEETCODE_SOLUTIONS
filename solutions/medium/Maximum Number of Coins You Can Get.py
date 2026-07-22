// Title: Maximum Number of Coins You Can Get
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        a = collections.deque(piles)
        count = 0 
        while len(a) > 0 :


        
            a.popleft()
            a.pop()
            count += a[-1]
            a.pop()
        return count 
        
