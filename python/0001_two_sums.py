# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_range = range(len(nums))
        for idx0 in nums_range:
            for idx1 in nums_range:
                if idx0 == idx1:
                    continue
                if nums[idx0] + nums[idx1] == target:
                    return sorted([idx0, idx1])

class TwoSumTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_twoSum(self):
        self.assertEqual(sorted(self.sol.twoSum([2, 7, 11, 15], 9)), [0, 1])
        self.assertEqual(sorted(self.sol.twoSum([2, 7, 11, 15], 18)), [1, 2])
        self.assertEqual(sorted(self.sol.twoSum([2, 7, 11, 15], 17)), [0, 3])
        self.assertEqual(sorted(self.sol.twoSum([2, 7, 11, 15], 13)), [0, 2])
