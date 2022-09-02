"""
Question Link
    https://leetcode.com/problems/count-primes/
"""
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[True]*n
        if n<=1:
            return 0
        a[0]=False
        a[1]=False
        count=0
        i=2
        while i*i<n:
            if a[i*i]==False:
                i+=1
                continue
            for j in range(i*i,n,i):
                a[j]=False
            i+=1
        for primes in a:
            if primes:
                count+=1
        return count
        