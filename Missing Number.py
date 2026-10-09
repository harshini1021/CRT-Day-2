class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        t=n*(n+1)//2
        ans=t-sum(nums)
        return ans