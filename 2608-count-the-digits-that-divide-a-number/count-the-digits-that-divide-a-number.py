class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        temp=num

        while temp>0:
            if num%(temp%10)==0:
                count+=1
            temp//=10
        
        return count