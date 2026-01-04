# Problem: Two Sum
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum

# Approach: Use a hash map to store numbers and their indices as we iterate through the array. For each number, calculate its complement (target - current number) and check if the complement exists in the hash map. If found, return the current index and the stored index of the complement. If not found, store the current number and its index in the hash map and continue.
# Time Complexity: <O(n)
# Space Complexity: O(n)+1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        hashmap = {}
        while i <= len(nums)-1:
            current = nums[i]
            complement = target-current
            if complement not in hashmap:
                hashmap[current] = i
            else:
                return [i,hashmap[complement]]
            i = i+1
            
