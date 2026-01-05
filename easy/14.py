# Problem: Longest Common Prefix
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-common-prefix/

# Approach: Find the shortest string length, then compare characters at each position across all strings
# Time Complexity: O(S) where S is the sum of all characters in all strings
# Space Complexity: O(1) excluding the output string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        least = 201
        curr = ""
        x = ""
        for i in range(len(strs)):
            if len(strs[i]) <= least:
                least = len(strs[i])
        for i in range(least):
            for e in range(1,len(strs)):
                previous_word = strs[e-1]
                current_word = strs[e]
                if previous_word[i] != current_word[i]:
                    return result
                x = current_word[i]
            result += x
        if least == 1:
            return strs[0][0]
        return result
