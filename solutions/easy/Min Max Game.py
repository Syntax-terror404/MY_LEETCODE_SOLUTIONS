// Title: Min Max Game
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/min-max-game/

        while len(nums) > 1:
            new = []
            for i in range(0, len(nums), 2):
                if i % 4 == 0:
                    new.append(min(nums[i], nums[i + 1]))
                else:
                    new.append(max(nums[i], nums[i + 1]))
            nums = new
    def minMaxGame(self, nums):
        return nums[0]
