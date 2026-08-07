// Title: Sum of Values at Indices With K Set Bits
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        result = []
        for i,num in enumerate(nums):
            if bin(i).count('1') == k:
                result.append(num)
        return sum(result)
            
