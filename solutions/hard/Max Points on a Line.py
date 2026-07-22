// Title: Max Points on a Line
            // Difficulty: Hard
            // Language: Python
            // Link: https://leetcode.com/problems/max-points-on-a-line/

        
        n = len(points)
        best = 1
        for i in range(n):
            slopes = {}
            for j in range(n):
                if i == j: continue
                dx, dy = points[j][0]
                -points[i][0], points[j]
                [1]-points[i][1]
                g = gcd(dx, dy) or 1
                dx, dy = dx//g, dy//g
                if dx < 0: dx, dy = -dx, 
                -dy
                slopes[(dx, dy)] = 
