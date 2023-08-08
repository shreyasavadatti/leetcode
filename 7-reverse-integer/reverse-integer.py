class Solution(object):
    def reverse(self, x):
        if x>=0:
            sign=1
        else: 
            sign=-1
        x=abs(x)
        rev=0
        while x!=0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev>2**31-1:
            return 0
        else:
            return sign*rev
