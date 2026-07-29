// Title: Top K Frequent Elements
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/top-k-frequent-elements/

        freq = [[]for i in range(len
        (nums)+ 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 
            0)
        for n, c in count.items():
            freq[c].append(n)
