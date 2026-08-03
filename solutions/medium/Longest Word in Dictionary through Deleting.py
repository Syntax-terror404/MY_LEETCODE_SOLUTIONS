// Title: Longest Word in Dictionary through Deleting
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

    def is_subsequence(self, word, s):
        j = 0
        for char in s:
            if j < len(word) and char == word[j]:
                j += 1
        return j == len(word)
