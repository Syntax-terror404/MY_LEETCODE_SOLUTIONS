// Title: Evaluate Reverse Polish Notation
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(float(a )/ b))
                    
        return stack[0]
