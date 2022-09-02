"""
Question Link
    https://leetcode.com/problems/3sum/
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()    
        triplets=list()
        i=0
        while i<len(nums):
            a=-nums[i]
            lo=i+1
            hi=len(nums)-1
            while lo<hi:
                s=nums[lo]+nums[hi]
                if s==a:
                    triplets.append([nums[lo],nums[hi],-a])
                    while lo<hi and nums[lo]==nums[lo+1]:
                        lo+=1
                    while lo<hi and nums[hi]==nums[hi-1]:
                        hi-=1
                    lo+=1
                    hi-=1
                elif s<a:
                    lo+=1
                else:
                    hi-=1
                    
            i+=1
            while i<len(nums) and nums[i]==-a:
                i+=1
        return triplets
                
                