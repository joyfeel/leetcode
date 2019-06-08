class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums.sort()
        return sum(nums[::2])561. Array Partition I