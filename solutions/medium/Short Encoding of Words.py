// Title: Short Encoding of Words
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/short-encoding-of-words/

class Solution(object):
    def minimumLengthEncoding(self, words):
        # Step 1: Put all words into a set to remove exact 
        duplicates
        word_set = set(words)
        
        # Step 2: For every word, check if it is a suffix of 
        any OTHER word.
        # If it is, we don't need to encode it separately, so 
        remove it.
        for word in words:
            for i in range(1, len(word)):
                # word[i:] is every possible suffix of 'word'
