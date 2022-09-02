"""
Question Link
    https://leetcode.com/problems/rotate-array/
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        temp=[0]*len(nums)
        if k>len(nums):
            k=k%len(nums)
        i=len(nums)-k
        s=0
        while i<len(nums):
            temp[s]=nums[i]
            i+=1
            s+=1
        i=0
        s=k
        while i<len(nums)-k:
            temp[s]=nums[i]
            i+=1
            s+=1
        for i in range(len(nums)):
            nums[i]=temp[i]
            