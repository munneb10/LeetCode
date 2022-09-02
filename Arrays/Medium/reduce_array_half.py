"""
Question Link
    https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        numbers_count={}
        df=len(arr)
        for i in arr:
            if numbers_count.get(i) is None:
                numbers_count[i]=1
            else:
                numbers_count[i]+=1
        l = list(numbers_count.values())
        l.sort(reverse = True)
        c=0
        for ele in l:
            df-=ele
            c+=1
            if(df<=len(arr)/2):
                break
        return c
            