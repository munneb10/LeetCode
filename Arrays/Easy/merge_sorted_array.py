"""
Question Link
https://leetcode.com/problems/merge-sorted-array/
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p=m+n-1
        m-=1
        n-=1
        while p>=0:
            if  m<0 or n>=0 and nums1[m]<=nums2[n]:
                nums1[p]=nums2[n]
                p-=1
                n-=1
            else:
                nums1[p]=nums1[m]
                p-=1
                m-=1