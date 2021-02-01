//Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = sum = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                res = min(res,i-l+1)
                sum -= nums[l]
                l = l+1
        return res if res <= len(nums) else 0
