// Title: Existence of a Substring in a String and Its Reverse
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

        for i in range(len(s) - 1):
        rec = s[::-1]
            ss = s[i:i+2]
            if ss in rec:
                return True
        return False
        
