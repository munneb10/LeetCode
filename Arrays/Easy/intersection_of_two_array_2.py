"""
Question Link
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        a={}
        for num in nums1:
            if a.get(num) is None:
                a[num]=1
            else:
                a[num]+=1
        inter=[]
        for num in nums2:
            if a.get(num):
                if a[num]>0:
                    inter.append(num)
                    a[num]-=1
        return inter
            