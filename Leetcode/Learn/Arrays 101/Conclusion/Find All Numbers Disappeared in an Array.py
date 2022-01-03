"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/


Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


-> Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

-> Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
1. n == nums.length
2. 1 <= n <= 10^5
3. 1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Find disappear numbers."""
        s = set(nums)
        return [num for num in range(1, len(nums) + 1) if num not in s]
