class Solution:
    def isPalindrome(self, x: int) -> bool: 
        n=x
        reverse=0
        while(n>0):
            digit=n%10
            reverse=reverse*10+digit
            n=n//10
        if(reverse==x):
            return True
        else:
            return False