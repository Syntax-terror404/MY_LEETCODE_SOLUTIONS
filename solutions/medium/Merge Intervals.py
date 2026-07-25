// Title: Merge Intervals
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

            else:
                merged.append(interval)
