// Title: Product of Array Except Self
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/product-of-array-except-self/

        pre = 1 
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        pos = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos 
            pos *= nums[i]
        return res 
       
