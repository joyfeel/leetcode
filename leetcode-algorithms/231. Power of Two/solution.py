#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 2 == 0:
            n /= 2

        return True if n == 1 else False

  