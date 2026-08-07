// Title: Min Stack
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value): 
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack
        [-1]:
