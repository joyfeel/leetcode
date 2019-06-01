#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        nums_length = range(len(nums))
        for i in nums_length:
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        # nums = nums[0: index]
        return index