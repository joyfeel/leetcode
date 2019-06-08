#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        
        if N == 1:
            return 1

        if N > 1:
            return self.fib(N - 1) + self.fib(N - 2)

