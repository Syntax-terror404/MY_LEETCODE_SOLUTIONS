// Title: Maximum Product of Two Digits
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        pro = []
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                pro.append(digits[i] * digits[j])
        return max(pro)
