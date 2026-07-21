// Title: Count Operations to Obtain Zero
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution(object):
    def countOperations(self, num1, num2):
        count = 0 
                num2 -= num1
                num1 -= num2
            count += 1
        while num1 != 0 and num2 != 0:
            if num1 < num2: 
            else:
        return count 
