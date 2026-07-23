// Title: Minimum Operations to Exceed Threshold Value I
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution(object):
    def minOperations(self, nums, k):
        count = 0 
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < k:
                i += 1
                count += 1 
        return count 
        
