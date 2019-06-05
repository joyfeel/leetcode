#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        new = 0
        tmp = x
        while x != 0:
            remainder = x % 10
            new = new * 10 + remainder
            x //= 10

        return tmp == new