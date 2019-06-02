#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        current = None
        nums_length = range(len(nums))
        for i in nums_length:
            if current != nums[i]:
                nums[index] = nums[i]
                current = nums[i]
                index += 1
        # nums = nums[0 : index]
        return index