// Title: Valid Anagram
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/valid-anagram/

        letters2 = {}
        for char in s:
            letters1[char] = letters1.get(char, 0) + 1
            letters2[char] = letters2.get(char, 0) + 1
        if letters1 == letters2:
        letters1 = {}
            return False
        if len(s) != len(t):
    def isAnagram(self, s, t):
class Solution(object):
        for char in t:
