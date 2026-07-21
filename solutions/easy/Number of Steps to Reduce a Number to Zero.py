// Title: Number of Steps to Reduce a Number to Zero
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

        while num != 0:
            if num % 2 != 0:
                num -= 1
            else:
                num //= 2
            count += 1 
        count = 0 
    def numberOfSteps(self, num):
class Solution(object):
