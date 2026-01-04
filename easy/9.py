# Problem: Palindrome
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome

# Approach: Convert the integer to a string and check if the string reads the same forwards and backwards. Alternatively, extract digits by repeatedly taking modulo 10 and dividing by 10, then compare the digits from both ends moving inward.
# Time Complexity: O(n)
# Space Complexity: O(n)

#1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10 and x > -1:
            return True
        digitsArray = []
        temp = x
        while temp != 0:
            digitsArray.append(temp%10)
            temp = int(temp/10)
        i = 0
        j = len(digitsArray)-1
        while i < j:
            if digitsArray[i] != digitsArray[j]:
                return False
            i += 1
            j -= 1
        return True

#2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp != 0:
            rev = rev * 10 + temp%10
            temp = temp//10
        return rev == x