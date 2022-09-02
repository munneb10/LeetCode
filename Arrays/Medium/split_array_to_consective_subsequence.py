"""
Question Link
    https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""
class Solution(object):
    def isPossible(self, nums):
        
        seq = defaultdict(int)
        left = Counter(nums)
        
        for num in nums:
            if (not left[num]): continue 
            if (seq[num-1] > 0):
                seq[num-1] -= 1 
                seq[num] += 1
                left[num] -= 1                
            else:
                if (not left[num+1] or not left[num+2]):
                                return False
                left[num] -= 1
                left[num+1] -= 1
                left[num+2] -= 1
                seq[num+2] += 1
        
        return True