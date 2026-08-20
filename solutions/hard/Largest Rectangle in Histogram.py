// Title: Largest Rectangle in Histogram
            // Difficulty: Hard
            // Language: Python
            // Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

        self.tree = [0] * (2 * self.n)
        self.build()
        self.A = A
        while (self.n & (self.n - 1)) != 0:
            self.A.append(self.INF)
            self.n += 1
class MinIdx_Segtree:
    def __init__(self, N, A):
        self.n = N
        self.INF = int(1e9)
