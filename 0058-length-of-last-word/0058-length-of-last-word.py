class Solution:
    def lengthOfLastWord(self, s):
        i=len(s)-1
        while s[i]==' ':
            i-=1
        l=0
        while i>=0 and s[i]!=' ':
            l+=1
            i-=1
        return l