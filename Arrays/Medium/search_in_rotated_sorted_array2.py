"""
Question Link
    https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        m=0
        while(l<=r):
            m=(l+r)//2
            if target==nums[m]:
                return True
            if (nums[l] == nums[m]) and (nums[r] == nums[m]):
                l, r = l+1, r-1
                continue
            if nums[l]<=nums[m]:
                if target<nums[m]:
                    if target>=nums[l]:
                        r=m-1
                    else:
                        l=m+1
                else:
                    l=m+1
            else:
                if target>nums[m]:
                    if target>nums[r]:
                        r=m-1
                    else:
                        l=m+1
                else:
                    r=m-1
        return False