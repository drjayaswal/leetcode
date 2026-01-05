# Problem: Roman to Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/roman-to-integer

# Approach: Use a hash map to store Roman numeral values. Iterate through the string and compare each character with the next one. If the current value is less than the next value, it's a subtractive case (like IV = 4), so subtract current from next and skip both characters. Otherwise, add the current value to the result and move to the next character.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if s in nums:
            return nums[s[0]]
        n = len(s)
        ans = 0
        i = 0
        while i < n-1:
            next_value = nums[s[i+1]]
            current_value = nums[s[i]]
            if current_value >= next_value:
                ans += current_value
                i+=1
            else:
                ans += next_value - current_value
                i+=2
            if i == n-1:
                ans += nums[s[i]]
        return ans
