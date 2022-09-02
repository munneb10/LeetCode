"""
Question Link
    https://leetcode.com/problems/jump-game/
"""
# Worst approach  
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        zero_occ=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zero_occ.append(i)
        
        for zc in range(len(zero_occ)):
            cind=zero_occ[zc]-1
            poss=False
            while cind>=0:
                if cind+nums[cind]>zero_occ[zc] or cind+nums[cind]==len(nums)-1:
                    poss=True
                    break
                cind-=1
            if not poss:
                return False
        return True