"""
Question Link
https://leetcode.com/problems/unique-morse-code-words/
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniqueTrans=0
        a={}
        for word in words:
            cons=""
            for w in word:
                cons+=codes[ord(w)%97]
            if a.get(cons) is None:
                a[cons]=0
                uniqueTrans+=1
        return uniqueTrans