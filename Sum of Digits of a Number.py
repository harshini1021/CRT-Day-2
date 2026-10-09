class Solution:
    def sumOfDigits(self, n):
        sum=0
        while n!=0:
            d=n%10
            sum+=d
            n=n//10
        return sum