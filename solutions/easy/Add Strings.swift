// Title: Add Strings
            // Difficulty: Easy
            // Language: Swift
            // Link: https://leetcode.com/problems/add-strings/

        
        while i >= 0 || j >= 0 || carry > 0 {
            let digitA = i >= 0 ? Int(a[i].asciiValue! - 
            zeroAscii) : 0
            let digitB = j >= 0 ? Int(b[j].asciiValue! - 
            zeroAscii) : 0
            
        
        let zeroAscii = Character("0").asciiValue!
