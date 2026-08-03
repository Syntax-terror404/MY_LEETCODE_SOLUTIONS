// Title: Longest Word in Dictionary
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/longest-word-in-dictionary/

                if len(word) > len(best) or (len(word) == len(best) and word < 
                best):
                    best = word
        
        return best
