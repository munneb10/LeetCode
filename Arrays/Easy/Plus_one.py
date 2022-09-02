"""
Question Link
https://leetcode.com/problems/plus-one/
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=len(digits)-1
        if digits[l]!=9:
            digits[l]+=1
        else:
            while(l!=-1 and digits[l]==9):
                digits[l]=0
                l-=1
            if l==-1:
                digits.insert(0,1)
            else:
                digits[l]+=1
        return digits