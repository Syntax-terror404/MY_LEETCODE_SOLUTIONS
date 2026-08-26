// Title: Trapping Rain Water
            // Difficulty: Hard
            // Language: Python
            // Link: https://leetcode.com/problems/trapping-rain-water/

                count += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax,height[r])
                count += rightmax - height[r]
        return count
