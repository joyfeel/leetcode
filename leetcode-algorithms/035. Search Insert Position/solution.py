#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        length_of_nums = len(nums)

        if target > nums[length_of_nums - 1]:
            return length_of_nums

        if target <= nums[0]:
            return 0 

        for i  in range(1, length_of_nums):
            if nums[i] >= target:
                return i