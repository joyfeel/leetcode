
# @lc app=leetcode id=189 lang=python3

# [189] Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1, Time Complexity O(n), Space Complexity O(n)
        # 
        # length_arr = len(nums)
        # k %= len(nums)
        # nums[:k], nums[k:] = nums[length_arr - k:], nums[:length_arr - k]

        # Solution 2, Time Complexity O(n), Space Complexity O(1)
        # http://laker.me/blog/2019/03/20/19_0320_leetcode189/
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n 
        numReverse(0, n - 1)
        numReverse(0, k - 1)
        numReverse(k, n - 1)