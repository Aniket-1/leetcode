//Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while(l<=h):
            m = (l+h)//2
            if nums[m] == target:
                return m
            if nums[m]<target:
                l = m+1  
            else:
                h = m-1
        return l
