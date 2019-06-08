#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        data = [];
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                data.append('FizzBuzz')
            elif i % 3 == 0:
                data.append('Fizz')
            elif i % 5 == 0:
                data.append('Buzz')        
            else:
                data.append(str(i))

        return data
