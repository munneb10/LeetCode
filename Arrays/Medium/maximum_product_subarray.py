"""
Question Link
    https://leetcode.com/problems/maximum-product-subarray/
"""
class Solution(object):        
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        currPro=1
        ans=min(nums)
        for n in nums:
            currPro*=n
            ans=max(ans,currPro,n)
            if currPro==0:
                currPro=1
        currPro=1
        for i in range(l-1,0,-1):
            currPro*=nums[i]
            ans=max(ans,currPro,n)
            if currPro==0:
                currPro=1
        return ans
            