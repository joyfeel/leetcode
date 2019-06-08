#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_list = [ c for c in s.lower() if c.isalnum() ]

        return clean_list == clean_list[::-1]

