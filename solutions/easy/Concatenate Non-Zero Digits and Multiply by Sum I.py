// Title: Concatenate Non-Zero Digits and Multiply by Sum I
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution(object):
    def sumAndMultiply(self, n):
        digits = [d for d in str(abs(n)) if d != '0']
        if not digits:
            return 0 
        x = int(''.join(digits))
        total = sum(int(d) for d in str(x))
        return x*total 
        
