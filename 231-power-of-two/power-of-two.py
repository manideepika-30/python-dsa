class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        
        value=1

        while value<n:
            value=value*2

        return value==n