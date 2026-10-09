class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        freq={}
        for i in nums:
          freq[i]=freq.get(i,0)+1
        for key,value in freq.items():
          if(value>n/2):
            return key