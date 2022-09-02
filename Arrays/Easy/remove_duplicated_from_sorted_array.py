"""
Question Link
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        curr_pos=1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                nums[curr_pos]=nums[i];
                curr_pos+=1
            i+=1
        return curr_pos
        